from sopn_publish_date import StatementPublishDate
from sopn_publish_date.calendars import Country, Region
from sopn_publish_date.election_ids import (
    InvalidElectionIdError,
    AmbiguousElectionIdError,
    NoSuchElectionTypeError,
)

from datetime import date
from pytest import raises

sopn_publish_date = StatementPublishDate()


def test_publish_date_local_id():

    with raises(AmbiguousElectionIdError) as err:
        sopn_publish_date.for_id("local.2019-02-21")

    assert str(err.value) == "Cannot derive country from election id [local.2019-02-21]"


def test_publish_date_local_id_with_country():
    publish_date = sopn_publish_date.for_id("local.2019-02-21", country="ENG")

    assert publish_date == date(2019, 1, 28)


def test_publish_date_parl_id_with_country():
    publish_date = sopn_publish_date.for_id("parl.2019-02-21", country="ENG")

    assert publish_date == date(2019, 1, 25)


def test_publish_date_parl_id_with_invalid_country():

    with raises(AmbiguousElectionIdError) as err:
        sopn_publish_date.for_id("parl.2019-02-21", country="USA")

    assert (
        str(err.value)
        == "Election id [parl.2019-02-21] requires a valid country, got [USA]"
    )


def test_publish_date_not_an_election_type():

    with raises(NoSuchElectionTypeError) as err:
        sopn_publish_date.for_id("not-an-election.2019-02-21")

    assert str(err.value) == "Election type [not-an-election] does not exist"


def test_publish_date_id_that_does_not_need_country():
    publish_date = sopn_publish_date.for_id("naw.c.ceredigion.2016-05-05")

    assert publish_date == date(2016, 4, 7)


def test_publish_date_invalid_id():

    with raises(InvalidElectionIdError) as err:
        sopn_publish_date.for_id("not an election id")

    assert (
        str(err.value) == "Parameter [not an election id] is not in election id format"
    )


def test_publish_date_invalid_date():

    with raises(InvalidElectionIdError) as err:
        sopn_publish_date.for_id("parl.not-a-date")

    assert str(err.value) == "Parameter [parl.not-a-date] is not in election id format"


# Reference election: sp.c.shetland-islands.2016-05-05
def test_publish_date_scottish_parliament():
    publish_date = sopn_publish_date.scottish_parliament(date(2016, 5, 5))

    assert publish_date == date(2016, 4, 1)


# Reference election: naw.c.ceredigion.2016-05-05
def test_publish_date_national_assembly_of_wales():
    publish_date = sopn_publish_date.national_assembly_for_wales(date(2016, 5, 5))

    assert publish_date == date(2016, 4, 7)


def test_publish_date_european_parliament():
    publish_date = sopn_publish_date.european_parliament(
        date(2019, 5, 23), region=Region.LONDON
    )

    assert publish_date == date(2019, 4, 25)


def test_publish_date_european_parliament_south_west_england():
    publish_date = sopn_publish_date.european_parliament(
        date(2019, 5, 23), region=Region.SOUTH_WEST_ENGLAND
    )

    assert publish_date == date(2019, 4, 24)


# Reference election: gla.c.barnet-and-camden.2016-05-05
def test_publish_date_greater_london_assembly():
    publish_date = sopn_publish_date.greater_london_assembly(date(2016, 5, 5))

    assert publish_date == date(2016, 4, 1)


# Reference election: nia.belfast-east.2017-03-02
def test_publish_date_northern_ireland_assembly():
    publish_date = sopn_publish_date.northern_ireland_assembly(date(2017, 3, 2))

    assert publish_date == date(2017, 2, 8)


# Reference election: pcc.avon-and-somerset.2016-05-05
def test_publish_date_police_and_crime_commissioner():
    publish_date = sopn_publish_date.police_and_crime_commissioner(date(2016, 5, 5))

    assert publish_date == date(2016, 4, 8)


# Reference election: local.highland.wester-ross-strathpeffer-and-lochalsh.by.2018-12-06
def test_publish_date_scottish_local():
    publish_date = sopn_publish_date.local(date(2018, 12, 6), country=Country.SCOTLAND)

    assert publish_date == date(2018, 11, 2)


# Reference election: local.belfast.balmoral.2019-05-02
def test_publish_date_northern_ireland_local():
    publish_date = sopn_publish_date.local(
        date(2019, 5, 2), country=Country.NORTHERN_IRELAND
    )

    assert publish_date == date(2019, 4, 8)


# Reference election: local.herefordshire.ross-north.2019-06-06
def test_publish_date_local_election_england():
    publish_date = sopn_publish_date.local(date(2019, 6, 6), country=Country.ENGLAND)

    assert publish_date == date(2019, 5, 10)


# Reference election: mayor.liverpool-city-ca.2017-05-04
def test_publish_date_mayor():
    publish_date = sopn_publish_date.mayor(date(2017, 5, 4))

    assert publish_date == date(2017, 4, 4)


# Reference election: mayor.london.2016-05-05
def test_publish_date_mayor_london():
    publish_date = sopn_publish_date.greater_london_assembly(date(2016, 5, 5))

    assert publish_date == date(2016, 4, 1)


# Reference election: parl.aberavon.2017-06-08
def test_publish_date_uk_parliament_wales():
    publish_date = sopn_publish_date.uk_parliament(
        date(2017, 6, 8), country=Country.WALES
    )

    assert publish_date == date(2017, 5, 11)


# Reference election: parl.na-h-eileanan-an-iar.2017-06-08
def test_publish_date_uk_parliament_scotland():
    publish_date = sopn_publish_date.uk_parliament(
        date(2017, 6, 8), country=Country.SCOTLAND
    )

    assert publish_date == date(2017, 5, 11)


# Reference election: parl.belfast-east.2017-06-08
def test_publish_date_uk_parliament_northern_ireland():
    publish_date = sopn_publish_date.uk_parliament(
        date(2017, 6, 8), country=Country.NORTHERN_IRELAND
    )

    assert publish_date == date(2017, 5, 11)


# Reference election: parl.hemel-hempstead.2017-06-08
def test_publish_date_uk_parliament_england():
    publish_date = sopn_publish_date.uk_parliament(
        date(2017, 6, 8), country=Country.ENGLAND
    )

    assert publish_date == date(2017, 5, 11)


# Reference election: parl.aberdeen-north.2015-05-07
def test_publish_date_uk_parliament_scotland_2015():
    publish_date = sopn_publish_date.uk_parliament(
        date(2015, 5, 7), country=Country.SCOTLAND
    )

    assert publish_date == date(2015, 4, 9)
