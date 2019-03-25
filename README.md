# sopn-publish-date

[![Build Status](https://travis-ci.org/mrwilson/sopn-publish-date.svg?branch=master)](https://travis-ci.org/mrwilson/sopn-publish-date)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
> Given the polling day of an election in the UK, when should the Statement of Persons Nominated (SoPN) should be published?

This is a non-trivial question, depending on:

- type of election
- country
- calendars and bank holidays

Even then, it's fuzzy - if a candidate objects to their nomination, that can delay SoPN publication up to the next day.

This project answers when a SoPN _should_ be published, but that is not a guarantee that it _will_ be.

## Usage

`sopn_publish_date` defines a class `StatementPublishDate` with two functions:

* `for_id` takes a string `election_id` in [uk-election-ids](https://elections.democracyclub.org.uk/reference_definition/) format and:

    * Returns a `datetime` where the location of the election is unambiguous e.g. Scottish Parliamentary elections
    * Throws an exception where the location of the election is ambiguous e.g. `local`, `parl`
* `for_country` takes a string `country` and a `datetime` and:
    * Returns a `datetime` where the country is in the united kingdom
    * Throws an exception where the country is unknown

Examples:

```python
from sopn_publish_date import StatementPublishDate
from datetime import datetime

sopn_publish_date = StatementPublishDate()

# Taking an id
sopn_publish_date.for_id('nia.belfast-east.2017-03-02')

# Taking a country and date
sopn_publish_date.for_country('scotland', datetime(2019, 2, 23))
```

## Test

`python -m pytest -v`

## Sources

The [bank holidays JSON](./sopn_publish_date/bank-holidays.json) is provided by [gov.uk](https://www.gov.uk/bank-holidays.json) under the [Open Government Licence](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)

## Todo

Election types:

 - [x] Local
 - [x] Parliament
 - [x] Scottish Parliament
 - [x] National Assembly for Wales
 - [x] Northern Irish Assembly
 - [x] Mayoral
 - [ ] EU parliament
 - [x] Greater London Assembly
 - [x] Police and Crime commissioner
 
Calendars:
 - [x] England + Wales
 - [x] Scotland
 - [x] Northern Ireland
 - [x] Fixed-date bank holidays e.g. royal weddings

## Useful Links (delete pre-1.0)

 * Association of Electoral Administrators [review of May 2016 elections](https://www.aea-elections.co.uk/wp-content/uploads/2016/09/aea-rep-2016-pushed-to-the-absolute-limit-the-electoral-year-never-to-forget-with-links.pdf) (Appendix D contains full timetabling for all concurrent elections)
 * TheyWorkForYou/Hansard: Lord Roberts of Llandudno on [overseas voting](https://www.theyworkforyou.com/lords/?id=2011-03-02a.1127.0)
 
## Relevant Legislation

 * [The Local Authorities (Mayoral Elections) (England and Wales) Regulations 2007](https://www.legislation.gov.uk/uksi/2007/1024/made) - timetables for mayoral elections (schedule 1, Timetable)
 * [The Police and Crime Commissioner Elections Order 2012](https://www.legislation.gov.uk/uksi/2012/1917/made) - timetables for police and crime commissioner elections (schedule 1, Timetable)
 * [Electoral Law Act (Northern Ireland) 1962](https://www.legislation.gov.uk/apni/1962/14/schedule/5/part/I) and [The Local Elections (Northern Ireland) Order 2010](https://www.legislation.gov.uk/uksi/2010/2977/schedule/1/part/4/made) - timetables for local elections in Northern Ireland
 * [The Greater London Authority Elections Rules 2007](http://www.legislation.gov.uk/uksi/2007/3541/contents/made) - timetables for London Assembly and Mayor of London.
 
 