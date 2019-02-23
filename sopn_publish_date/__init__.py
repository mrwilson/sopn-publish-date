from sopn_publish_date.calendars import working_days
from datetime import datetime


def sopn_publish_date(election_id):

    election_type, *_, poll_date = election_id.split(".")

    return _sopn_publish_date(election_type, datetime.strptime(poll_date, "%Y-%m-%d"))


def _sopn_publish_date(election_type, poll_date):

    if election_type in ["local", "parl"]:
        return poll_date - working_days(19)
    elif election_type == "sp":
        return poll_date - working_days(23)

    raise Exception("Not implemented for election type: %s" % election_type)
