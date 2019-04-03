import json
import os
from datetime import datetime, date

from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday
from pandas.tseries.offsets import CDay as BusinessDays
from enum import Enum


class Country(Enum):
    """
    The countries of the United Kingdom.
    """

    ENGLAND = 1
    NORTHERN_IRELAND = 2
    SCOTLAND = 3
    WALES = 4


class BankHolidayCalendar(AbstractHolidayCalendar):
    """
    A calendar that honours the standard 5-day week in addition to the input list of dates.
    """

    def __init__(self, dates):
        for bank_holiday in dates:
            bank_holiday_date = datetime.strptime(bank_holiday["date"], "%Y-%m-%d")
            self.rules.append(
                holiday_from_datetime(bank_holiday["title"], bank_holiday_date)
            )
        AbstractHolidayCalendar.__init__(self)


class UnitedKingdomBankHolidays(object):
    """
    A representation of the bank holiday calendars in the United Kingdom.

    This class exposes a function for each unique calendar: England & Wales, Northern Ireland, and Scotland.
    """

    _calendar = {}

    def __init__(self):
        bank_holiday_json = os.path.join(
            os.path.dirname(__file__), "bank-holidays.json"
        )

        with open(bank_holiday_json, "r") as data:
            json_calendar = json.loads(data.read())

            for country in json_calendar.keys():
                self._calendar[country] = BankHolidayCalendar(
                    json_calendar[country]["events"]
                )

    def england_and_wales(self) -> BankHolidayCalendar:
        """
        :return: a calendar representation of bank holidays in England and Wales
        """
        return self._calendar["england-and-wales"]

    def scotland(self) -> BankHolidayCalendar:
        """
        :return: a calendar representation of bank holidays in Scotland
        """
        return self._calendar["scotland"]

    def northern_ireland(self) -> BankHolidayCalendar:
        """
        :return: a calendar representation of bank holidays in Northern Ireland
        """
        return self._calendar["northern-ireland"]

    def from_country(self, country: Country) -> BankHolidayCalendar:
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


def working_days(count: int, calendar: BankHolidayCalendar) -> BusinessDays:
    """
    A pandas representation of a period with the given number of working days using a specified calendar.

    :param count: number of working days
    :param calendar: calendar representing bank holidays in a specific country
    :return: a number of days to be used in date arithmetic that honours weekends and bank holidays
    """
    return BusinessDays(count, calendar=calendar)


def as_date(timestamp) -> date:
    """
    Transforms a pandas._libs.tslibs.Timestamp into a datetime.date object

    :param timestamp: a pandas Timestamp object
    :return: the equivalent python date object
    """
    return timestamp.to_pydatetime().date()


def holiday_from_datetime(name: str, original_datetime: datetime) -> Holiday:
    """
    Transforms a named datetime.datetime into a pandas.tseries.holiday.Holiday

    :param name: the name of the holiday
    :param original_datetime: a representation of the holiday as a datetime
    :return: the pandas.tseries.holiday.Holiday representation of the datetime
    """
    return Holiday(
        name,
        year=original_datetime.year,
        month=original_datetime.month,
        day=original_datetime.day,
    )
