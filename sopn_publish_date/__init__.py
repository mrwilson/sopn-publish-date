from sopn_publish_date.calendars import working_days, UnitedKingdomBankHolidays, as_date

from datetime import datetime, date


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

            date_of_poll = datetime.strptime(poll_date, "%Y-%m-%d").date()

            return election_type, date_of_poll
        except Exception:
            raise InvalidElectionId(
                "Parameter [%s] is not in election id format" % election_id
            )

    def for_id(self, election_id):

        election_type, poll_date = StatementPublishDate._extract_from_id(election_id)

        if election_type == "nia":
            return self.northern_ireland_assembly(poll_date)
        elif election_type == "sp":
            return self.scottish_parliament(poll_date)
        elif election_type == "naw":
            return self.national_assembly_for_wales(poll_date)
        elif election_type == "gla" or "mayor.london" in election_id:
            return self.greater_london_assembly(poll_date)
        elif election_type == "pcc":
            return as_date(poll_date - working_days(18, self.calendar.england_and_wales()))
        elif election_type == "mayor":
            return as_date(poll_date - working_days(19, self.calendar.england_and_wales()))
        else:
            raise AmbiguousElectionId(
                "Cannot derive country from election id [%s]" % election_id
            )

    def northern_ireland_assembly(self, poll_date: date) -> date:
        """
        Calculate the publish date for an election to the Northern Ireland Assembly

        This is set out by Schedule 5, Rules 1 and 2 of `The Northern Ireland Assembly (Elections) (Amendment) Order 2009 <https://www.legislation.gov.uk/uksi/2009/256/made>`_

        :param poll_date: a datetime representing the date of the poll
        :return: a datetime representing the expected publish date
        """
        return as_date(poll_date - working_days(16, self.calendar.northern_ireland()))

    def scottish_parliament(self, poll_date: date) -> date:
        """
        Calculate the publish date for an election to the Scottish Parliament

        This is set out in `The Scottish Parliament (Elections etc.) Order 2015 <https://www.legislation.gov.uk/ssi/2015/425/made>`_

        :param poll_date: a datetime representing the date of the poll
        :return: a datetime representing the expected publish date
        """
        return as_date(poll_date - working_days(23, self.calendar.scotland()))

    def national_assembly_for_wales(self, poll_date: date) -> date:
        """
        Calculate the publish date for an election to the National Assembly for Wales

        This is set out in `The National Assembly for Wales (Representation of the People) (Amendment) Order 2016 <https://www.legislation.gov.uk/uksi/2016/272/article/18/made>`_

        :param poll_date: a datetime representing the date of the poll
        :return: a datetime representing the expected publish date
        """
        return as_date(poll_date - working_days(19, self.calendar.england_and_wales()))

    def greater_london_assembly(self, poll_date: date) -> date:
        """
        Calculate the publish date for an election to the Greater London Assembly

        This is set out in `The Greater London Authority Elections (Amendment) Rules 2016 <https://www.legislation.gov.uk/uksi/2016/24/article/6/made>`_

        :param poll_date: a datetime representing the date of the poll
        :return: a datetime representing the expected publish date
        """
        return as_date(poll_date - working_days(23, self.calendar.england_and_wales()))

    def police_and_crime_commissioner(self, poll_date: date) -> date:
        return as_date(poll_date - working_days(18, self.calendar.northern_ireland()))

    def for_country(self, country, poll_date: date) -> date:

        if country == "northern-ireland":
            return as_date(poll_date - working_days(16, self.calendar.northern_ireland()))
        elif country == "scotland":
            return as_date(poll_date - working_days(23, self.calendar.scotland()))
        elif country == "england" or country == "wales":
            return as_date(poll_date - working_days(19, self.calendar.england_and_wales()))
        else:
            raise Exception(
                "Not implemented for election: [%s,%s]" % (country, poll_date)
            )
