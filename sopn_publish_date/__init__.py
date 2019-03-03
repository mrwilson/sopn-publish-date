from sopn_publish_date.calendars import working_days, UnitedKingdomBankHolidays

from datetime import datetime


class StatementPublishDate(object):
    def __init__(self):
        self.calendar = UnitedKingdomBankHolidays()

    def for_id(self, election_id):

        election_type, *_, poll_date = election_id.split(".")

        date_of_poll = datetime.strptime(poll_date, "%Y-%m-%d")

        if election_type == "nia":
            return self.for_country("northern-ireland", date_of_poll)
        elif election_type == "sp":
            return self.for_country("scotland", date_of_poll)
        elif election_type == "naw":
            return self.for_country("wales", date_of_poll)
        elif election_type == "gla":
            return date_of_poll - working_days(23, self.calendar.england_and_wales())
        elif election_type == "pcc":
            return date_of_poll - working_days(18, self.calendar.england_and_wales())
        else:
            raise Exception(
                "Cannot derive country from ambiguous election id [%s]" % election_id
            )

    def for_country(self, country, poll_date):

        if country == "northern-ireland":
            return poll_date - working_days(16, self.calendar.northern_ireland())
        elif country == "scotland":
            return poll_date - working_days(23, self.calendar.scotland())
        elif country == "england" or country == "wales":
            return poll_date - working_days(19, self.calendar.england_and_wales())
        else:
            raise Exception(
                "Not implemented for election: [%s,%d]" % (country, poll_date)
            )
