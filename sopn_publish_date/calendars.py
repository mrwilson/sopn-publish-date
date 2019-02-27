from pandas.tseries.offsets import CDay

from pandas.tseries.holiday import (
    AbstractHolidayCalendar,
    DateOffset,
    EasterMonday,
    GoodFriday,
    Holiday,
    MO,
    next_monday,
    next_monday_or_tuesday,
)


class ScottishHolidays(AbstractHolidayCalendar):
    rules = [
        Holiday("New Years Day", month=1, day=1, observance=next_monday),
        Holiday("2nd January", month=1, day=1, observance=next_monday),
        GoodFriday,
        Holiday(
            "Early May bank holiday", month=5, day=1, offset=DateOffset(weekday=MO(1))
        ),
        Holiday(
            "Spring bank holiday", month=5, day=31, offset=DateOffset(weekday=MO(-1))
        ),
        Holiday(
            "Summer bank holiday", month=8, day=1, offset=DateOffset(weekday=MO(1))
        ),
        Holiday("St Andrew's Day", month=11, day=30, observance=next_monday),
        Holiday("Christmas Day", month=12, day=25, observance=next_monday),
        Holiday("Boxing Day", month=12, day=26, observance=next_monday_or_tuesday),
    ]


class EnglandAndWalesHolidays(AbstractHolidayCalendar):
    rules = [
        Holiday("New Years Day", month=1, day=1, observance=next_monday),
        GoodFriday,
        EasterMonday,
        Holiday(
            "Early May bank holiday", month=5, day=1, offset=DateOffset(weekday=MO(1))
        ),
        Holiday(
            "Spring bank holiday", month=5, day=31, offset=DateOffset(weekday=MO(-1))
        ),
        Holiday(
            "Summer bank holiday", month=8, day=31, offset=DateOffset(weekday=MO(-1))
        ),
        Holiday("Christmas Day", month=12, day=25, observance=next_monday),
        Holiday("Boxing Day", month=12, day=26, observance=next_monday_or_tuesday),
    ]


class NorthernIrelandHolidays(AbstractHolidayCalendar):
    rules = [
        Holiday("New Years Day", month=1, day=1, observance=next_monday),
        Holiday("St Patrick's Day", month=3, day=18, observance=next_monday),
        GoodFriday,
        EasterMonday,
        Holiday(
            "Early May bank holiday", month=5, day=1, offset=DateOffset(weekday=MO(1))
        ),
        Holiday(
            "Spring bank holiday", month=5, day=31, offset=DateOffset(weekday=MO(-1))
        ),
        Holiday(
            "Battle of the Boyne / Orangemen's Day",
            month=7,
            day=12,
            observance=next_monday,
        ),
        Holiday(
            "Summer bank holiday", month=8, day=31, offset=DateOffset(weekday=MO(-1))
        ),
        Holiday("Christmas Day", month=12, day=25, observance=next_monday),
        Holiday("Boxing Day", month=12, day=26, observance=next_monday_or_tuesday),
    ]


def working_days(count, calendar):
    return CDay(count, calendar=calendar)
