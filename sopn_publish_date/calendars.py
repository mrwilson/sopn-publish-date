import json
import os
from datetime import datetime, date

from pandas.tseries.holiday import (
    AbstractHolidayCalendar,
    Holiday,
    GoodFriday,
    EasterMonday,
    next_monday,
    next_monday_or_tuesday,
    MO,
)
from pandas.tseries.offsets import CDay as BusinessDays, DateOffset
from enum import Enum


class Country(Enum):
    """
    The countries of the United Kingdom.
    """

    ENGLAND = 1
    NORTHERN_IRELAND = 2
    SCOTLAND = 3
    WALES = 4


class Region(Enum):
    """
    The regions of the United Kingdom and Gibraltar as elected in the EU Parliament
    """

    EAST_MIDLANDS = 1
    EAST_OF_ENGLAND = 2
    LONDON = 3
    NORTH_EAST_ENGLAND = 4
    NORTH_WEST_ENGLAND = 5
    NORTHERN_IRELAND = 6
    SCOTLAND = 7
    SOUTH_EAST_ENGLAND = 8
    SOUTH_WEST_ENGLAND = 9
    WALES = 10
    WEST_MIDLANDS = 11
    YORKSHIRE_AND_THE_HUMBER = 12


class BankHolidayCalendar(AbstractHolidayCalendar):
    pass


class UKBankHolidayCalendar(AbstractHolidayCalendar):
    """
    A calendar that honours the standard 5-day week in addition to the input list of dates.
    """

    @staticmethod
    def create_holiday_from_entry(entry: dict) -> Holiday:
        holiday_date = datetime.strptime(entry["date"], "%Y-%m-%d")
        return holiday_from_datetime(entry["title"], holiday_date)

    def __init__(self, dates):
        AbstractHolidayCalendar.__init__(self)

        self.rules = [
            UKBankHolidayCalendar.create_holiday_from_entry(entry) for entry in dates
        ]


class GibraltarBankHolidays(BankHolidayCalendar):
    """
    A calendar that represents the public holidays of Gibraltar.
    """

    def __init__(self):
        BankHolidayCalendar.__init__(
            self,
            rules=[
                Holiday("New Years Day", month=1, day=1, observance=next_monday),
                Holiday(
                    "Commonwealth Day", month=3, day=1, offset=DateOffset(weekday=MO(2))
                ),
                GoodFriday,
                EasterMonday,
                Holiday("Worker's Day", month=4, day=28, observance=next_monday),
                Holiday(
                    "Early May bank holiday",
                    month=5,
                    day=1,
                    offset=DateOffset(weekday=MO(1)),
                ),
                Holiday(
                    "Spring bank holiday",
                    month=5,
                    day=31,
                    offset=DateOffset(weekday=MO(-1)),
                ),
                Holiday(
                    "Queen's Birthday", month=6, day=1, offset=DateOffset(weekday=MO(2))
                ),
                Holiday(
                    "Summer bank holiday",
                    month=8,
                    day=31,
                    offset=DateOffset(weekday=MO(-1)),
                ),
                Holiday("Gibraltar Day", month=9, day=10, observance=next_monday),
                Holiday("Christmas Day", month=12, day=25, observance=next_monday),
                Holiday(
                    "Boxing Day", month=12, day=26, observance=next_monday_or_tuesday
                ),
            ],
        )


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
                self._calendar[country] = UKBankHolidayCalendar(
                    json_calendar[country]["events"]
                )

    def england_and_wales(self) -> BankHolidayCalendar:
        """
        :return: a calendar representation of bank holidays in England and Wales
        """
        return self._calendar["england-and-wales"]

    def gibraltar(self) -> BankHolidayCalendar:
        """
        :return: a calendar representation of bank holidays in Gibraltar
        """
        return GibraltarBankHolidays()

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
