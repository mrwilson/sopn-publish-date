import json
import os
from datetime import datetime

from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday
from pandas.tseries.offsets import CDay


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


class CalendarFromJson(AbstractHolidayCalendar):
    rules = []

    def __init__(self, dates):
        for bank_holiday in dates:
            bank_holiday_date = datetime.strptime(bank_holiday["date"], "%Y-%m-%d")
            self.rules.append(
                Holiday(
                    bank_holiday["title"],
                    year=bank_holiday_date.year,
                    month=bank_holiday_date.month,
                    day=bank_holiday_date.day,
                )
            )
        AbstractHolidayCalendar.__init__(self)


def working_days(count, calendar):
    return CDay(count, calendar=calendar)
