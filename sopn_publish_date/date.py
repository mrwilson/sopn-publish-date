from typing import List
from datetime import date, timedelta

SATURDAY = 5
SUNDAY = 6


class DateMatcher:
    def __init__(self, day, month, year=None, name=None):
        self.name = name
        self.month = month
        self.day = day
        self.year = year

    def matches(self, other: date):
        if self.day != other.day:
            return False

        if self.month != other.month:
            return False

        if self.year is not None and self.year != other.year:
            return False

        return True


def days_before(poll_date: date, days: int, ignore: List[DateMatcher] = []) -> date:
    while days > 0:
        poll_date -= timedelta(days=1)

        if poll_date.weekday() in [SATURDAY, SUNDAY]:
            continue

        if any([day.matches(poll_date) for day in ignore]):
            continue

        days -= 1

    return poll_date
