from typing import List
from datetime import date, timedelta

SATURDAY = 5
SUNDAY = 6


def days_before(poll_date: date, days: int, exempted_days: List[date] = []) -> date:
    while days > 0:
        poll_date -= timedelta(days=1)

        if (
            poll_date.weekday() not in [SATURDAY, SUNDAY]
            and poll_date not in exempted_days
        ):
            days -= 1

    return poll_date
