from sopn_publish_date.calendars import (
    working_days,
    UnitedKingdomBankHolidays,
    as_date,
    Country,
)
from sopn_publish_date.election_ids import type_and_poll_date, AmbiguousElectionId

from datetime import date


class StatementPublishDate(object):
    def __init__(self):
        self.election_id_lookup = {
            "nia": self.northern_ireland_assembly,
            "sp": self.scottish_parliament,
            "naw": self.national_assembly_for_wales,
            "gla": self.greater_london_assembly,
            "pcc": self.police_and_crime_commissioner,
            "mayor": self.mayor,
            "parl": self.uk_parliament
        }
        self.calendar = UnitedKingdomBankHolidays()

    def for_id(self, election_id: str) -> date:
        """
        Calculate the publish date for an election given in `uk-election-ids <https://elections.democracyclub.org.uk/reference_definition/>`_ format, or raise an exception if that election id is ambiguous (could correspond to elections in multiple countries with different electoral legislation)

        :param election_id: a string representing an election id in uk-election-ids format
        :return: a datetime representing the expected publish date
        """
        election_type, poll_date = type_and_poll_date(election_id)

        if election_type in self.election_id_lookup:
            return self.election_id_lookup[election_type](poll_date)
        else:
            raise AmbiguousElectionId(election_id)

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

    def european_parliament(self, poll_date: date) -> date:
        """
        Calculate the publish date for an election to the European Parliament

        This is set out in `The European Parliamentary Elections (Amendment) Regulations 2009 <https://www.legislation.gov.uk/uksi/2009/186/made>`_

        :param poll_date: a datetime representing the date of the poll
        :return: a datetime representing the expected publish date
        """
        return as_date(poll_date - working_days(19, self.calendar.england_and_wales()))

    def police_and_crime_commissioner(self, poll_date: date) -> date:
        """
        Calculate the publish date for an election to the position of Police and Crime Commissioner

        This is set out in `The Police and Crime Commissioner Elections (Amendment) Order 2014 <https://www.legislation.gov.uk/uksi/2014/921/article/31/made>`_

        :param poll_date: a datetime representing the date of the poll
        :return: a datetime representing the expected publish date
        """
        return as_date(poll_date - working_days(18, self.calendar.england_and_wales()))

    def mayor(self, poll_date: date) -> date:
        """
        Calculate the publish date for an election to the position of Mayor in England and Wales

        This is set out in `The Local Authorities (Mayoral Elections) (England and Wales) (Amendment) Regulations 2014 <https://www.legislation.gov.uk/uksi/2014/370/made>`_

        :param poll_date: a datetime representing the date of the poll
        :return: a datetime representing the expected publish date
        """
        return as_date(poll_date - working_days(19, self.calendar.england_and_wales()))

    def uk_parliament(self, poll_date: date, country: Country = Country.ENGLAND):
        """
        Calculate the publish date for an election to the Parliament of the United Kingdom

        This is set out in `Electoral Registration and Administration Act 2013 <https://www.legislation.gov.uk/ukpga/2013/6/section/14>`_

        :param poll_date: a datetime representing the date of the poll
        :param country: the country in which the election is being run
        :return: a datetime representing the expected publish date
        """
        return as_date(poll_date - working_days(19, self.calendar.from_country(country)))

    def local(self, poll_date: date, country: Country):
        """
        Calculate the publish date for a local election.

        This is set out in:

         * `The Local Elections (Principal Areas) (England and Wales) (Amendment) Rules 2014 <https://www.legislation.gov.uk/uksi/2014/494/made>`_
         * `The Local Elections (Northern Ireland) Order 2010 <https://www.legislation.gov.uk/uksi/2010/2977/schedule/1/part/4/made>`_
         * `The Scottish Local Government Elections Order 2011 <https://www.legislation.gov.uk/ssi/2011/399/made>`_

        :param poll_date: a datetime representing the date of the poll
        :param country: the country in which the election is being run
        :return: a datetime representing the expected publish date
        """

        country_specific_duration = {
            Country.ENGLAND: 19,
            Country.NORTHERN_IRELAND: 16,
            Country.SCOTLAND: 23,
            Country.WALES: 19,
        }

        days_prior = country_specific_duration[country]

        return as_date(
            poll_date - working_days(days_prior, self.calendar.from_country(country))
        )
