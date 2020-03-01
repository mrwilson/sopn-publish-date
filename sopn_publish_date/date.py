from datetime import date, timedelta

SATURDAY = 5
SUNDAY = 6


def days_before(poll_date: date, days: int) -> date:
    while days > 0:
        poll_date -= timedelta(days=1)

        if poll_date.weekday() not in [SATURDAY, SUNDAY]:
            days -= 1

    return poll_date
