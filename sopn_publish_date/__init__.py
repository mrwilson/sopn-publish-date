from sopn_publish_date.calendars import working_days, ScottishHolidays, EnglandAndWalesHolidays, NorthernIrelandHolidays
from datetime import datetime


def sopn_publish_date_for_id(election_id):

    election_type, *_, poll_date = election_id.split(".")

    date_of_poll = datetime.strptime(poll_date, "%Y-%m-%d")

    if election_type == 'nia':
        return sopn_publish_date('northern-ireland', date_of_poll)
    elif election_type == 'sp':
        return sopn_publish_date('scotland', date_of_poll)
    elif election_type == 'naw':
        return sopn_publish_date('wales', date_of_poll)
    elif election_type == 'gla':
        return date_of_poll - working_days(23)
    else:
        raise Exception("Cannot derive country from ambiguous election id [%s]" % election_id)


def sopn_publish_date(country, poll_date):

    if country == 'northern-ireland':
        return poll_date - working_days(19, calendar=NorthernIrelandHolidays())
    elif country == 'scotland':
        return poll_date - working_days(23, calendar=ScottishHolidays())
    elif country == 'england' or country == 'wales':
        return poll_date - working_days(19, calendar=EnglandAndWalesHolidays())
    else:
        raise Exception("Not implemented for election: [%s,%d]" % (country, poll_date))
