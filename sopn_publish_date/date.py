from datetime import date, timedelta


def days_before(poll_date: date, days: int) -> date:
    return poll_date - timedelta(days=days)
