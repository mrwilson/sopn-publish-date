import json
import os
from datetime import datetime

from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday
from pandas.tseries.offsets import CDay
from enum import Enum


class Country(Enum):
    ENGLAND = 1
    NORTHERN_IRELAND = 2
    SCOTLAND = 3
    WALES = 4


class UnitedKingdomBankHolidays(object):
    calendar = {}

    def __init__(self):
        bank_holiday_json = os.path.join(
            os.path.dirname(__file__), "bank-holidays.json"
        )

        with open(bank_holiday_json, "r") as data:
            json_calendar = json.loads(data.read())

            for country in json_calendar.keys():
                self.calendar[country] = CalendarFromJson(
                    json_calendar[country]["events"]
                )

    def england_and_wales(self):
        return self.calendar["england-and-wales"]

    def scotland(self):
        return self.calendar["scotland"]

    def northern_ireland(self):
        return self.calendar["northern-ireland"]

    def from_country(self, country: Country):
        if country == Country.ENGLAND or country == Country.WALES:
            return self.england_and_wales()
        elif country == Country.NORTHERN_IRELAND:
            return self.northern_ireland()
        else:
            return self.scotland()


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


def working_days(count, calendar):
    return CDay(count, calendar=calendar)


def as_date(timestamp):
    return timestamp.to_pydatetime().date()
