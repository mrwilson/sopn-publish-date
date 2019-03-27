from sopn_publish_date.calendars import working_days, UnitedKingdomBankHolidays

from datetime import datetime


class InvalidElectionId(BaseException):
    pass


class AmbiguousElectionId(BaseException):
    pass


class StatementPublishDate(object):
    def __init__(self):
        self.calendar = UnitedKingdomBankHolidays()

    @staticmethod
    def _extract_from_id(election_id):
        try:
            election_type, *_, poll_date = election_id.split(".")

            date_of_poll = datetime.strptime(poll_date, "%Y-%m-%d")

            return election_type, date_of_poll
        except Exception:
            raise InvalidElectionId(
                "Parameter [%s] is not in election id format" % election_id
            )

    def for_id(self, election_id):

        election_type, poll_date = StatementPublishDate._extract_from_id(election_id)

        if election_type == "nia":
            return self.northern_irish_assembly(poll_date)
        elif election_type == "sp":
            return self.scottish_parliament(poll_date)
        elif election_type == "naw":
            return self.national_assembly_for_wales(poll_date)
        elif election_type == "gla" or "mayor.london" in election_id:
            return poll_date - working_days(23, self.calendar.england_and_wales())
        elif election_type == "pcc":
            return poll_date - working_days(18, self.calendar.england_and_wales())
        elif election_type == "mayor":
            return poll_date - working_days(19, self.calendar.england_and_wales())
        else:
            raise AmbiguousElectionId(
                "Cannot derive country from election id [%s]" % election_id
            )

    def northern_irish_assembly(self, poll_date):
        return poll_date - working_days(16, self.calendar.northern_ireland())

    def scottish_parliament(self, poll_date):
        return poll_date - working_days(23, self.calendar.scotland())

    def national_assembly_for_wales(self, poll_date):
        return poll_date - working_days(19, self.calendar.england_and_wales())

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
