from typing import List
from datetime import date, timedelta

SATURDAY = 5
SUNDAY = 6


def days_before(poll_date: date, days: int, exempted_days: List[date] = []) -> date:
    while days > 0:
        poll_date -= timedelta(days=1)

        if poll_date.weekday() in [SATURDAY, SUNDAY]:
            continue

        if poll_date in exempted_days:
            continue

        days -= 1

    return poll_date
