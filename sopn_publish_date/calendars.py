import json
import os
from datetime import datetime

from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday
from pandas.tseries.offsets import CDay as BusinessDays
from enum import Enum


class Country(Enum):
    ENGLAND = 1
    NORTHERN_IRELAND = 2
    SCOTLAND = 3
    WALES = 4


class CalendarFromJson(AbstractHolidayCalendar):
    rules = []

    def __init__(self, dates):
        for bank_holiday in dates:
            bank_holiday_date = datetime.strptime(bank_holiday["date"], "%Y-%m-%d")
            self.rules.append(
                CalendarFromJson.holiday_from_datetime(
                    bank_holiday["title"], bank_holiday_date
                )
            )
        AbstractHolidayCalendar.__init__(self)

    @staticmethod
    def holiday_from_datetime(name, date):
        return Holiday(name, year=date.year, month=date.month, day=date.day)


class UnitedKingdomBankHolidays(object):
    _calendar = {}

    def __init__(self):
        bank_holiday_json = os.path.join(
            os.path.dirname(__file__), "bank-holidays.json"
        )

        with open(bank_holiday_json, "r") as data:
            json_calendar = json.loads(data.read())

            for country in json_calendar.keys():
                self._calendar[country] = CalendarFromJson(
                    json_calendar[country]["events"]
                )

    def england_and_wales(self) -> CalendarFromJson:
        """
        :return: a calendar representation of bank holidays in England and Wales
        """
        return self._calendar["england-and-wales"]

    def scotland(self) -> CalendarFromJson:
        """
        :return: a calendar representation of bank holidays in Scotland
        """
        return self._calendar["scotland"]

    def northern_ireland(self) -> CalendarFromJson:
        """
        :return: a calendar representation of bank holidays in Northern Ireland
        """
        return self._calendar["northern-ireland"]

    def from_country(self, country: Country) -> CalendarFromJson:
        """
        Return the bank holiday calendar for the input country.

        :param country: the country to retrieve the calendar for
        :return: the corresponding calendar
        """
        if country == Country.ENGLAND or country == Country.WALES:
            return self.england_and_wales()
        elif country == Country.NORTHERN_IRELAND:
            return self.northern_ireland()
        else:
            return self.scotland()


def working_days(count: int, calendar: CalendarFromJson) -> BusinessDays:
    """
    A pandas representation of a period with the given number of working days using a specified calendar.

    :param count: number of working days
    :param calendar: calendar representing bank holidays in a specific country
    :return: a number of days to be used in date arithmetic that honours weekends and bank holidays
    """
    return BusinessDays(count, calendar=calendar)


def as_date(timestamp):
    return timestamp.to_pydatetime().date()
