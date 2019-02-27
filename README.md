# sopn-publish-date

> Given the polling day of an election in the UK, when should the Statement of Persons Nominated (SoPN) should be published?

Turns out this is a non-trivial question, depending on:

- type of election
- country
- calendars and bank holidays

## Usage

This library defines a single function `sopn_publish_date` which takes a string `election_id` in [uk-election-ids](https://elections.democracyclub.org.uk/reference_definition/) format and:

* Returns a `datetime` where the location of the election is unambiguous e.g. Scottish Parliamentary elections
* Throws an exception where the location of the election is ambiguous e.g. `local`, `parl`

```python
from sopn_publish_date import sopn_publish_date

local_election_sopn = sopn_publish_date('local.cardiff.2019-02-21')

# datetime.datetime(2019, 1, 25)
```

## Test

`python -m pytest`

## Todo

Election types:

 - [x] Local
 - [x] Parliament
 - [x] Scottish Parliament
 - [x] National Assembly for Wales
 - [x] Northern Irish Assembly
 - [ ] Mayoral
 - [ ] EU parliament
 - [x] Greater London Assembly
 - [ ] Police and Crime commissioner
 
Calendars:
 - [x] England + Wales
 - [x] Scotland
 - [x] Northern Ireland
 - [ ] Fixed-date bank holidays e.g. royal weddings

## Useful Links (delete pre-1.0)

 * Association of Electoral Administrators [review of May 2016 elections](https://www.aea-elections.co.uk/wp-content/uploads/2016/09/aea-rep-2016-pushed-to-the-absolute-limit-the-electoral-year-never-to-forget-with-links.pdf) (Appendix D contains full timetabling for all concurrent elections)
 * TheyWorkForYou/Hansard: Lord Roberts of Llandudno on [overseas voting](https://www.theyworkforyou.com/lords/?id=2011-03-02a.1127.0)
 
 