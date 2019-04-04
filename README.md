# sopn-publish-date

[![Build Status](https://travis-ci.org/mrwilson/sopn-publish-date.svg?branch=master)](https://travis-ci.org/mrwilson/sopn-publish-date)
[![Documentation Status](https://readthedocs.org/projects/sopn-publish-date/badge/?version=latest)](https://sopn-publish-date.readthedocs.io/en/latest/overview.html?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

> Given the polling day of an election in the UK, when should the Statement of Persons Nominated (SoPN) be published?

When an election is called in the United Kingdom, the voting public must have access to the list of candidates who have been nominated to that post.

These documents are called Statements of Persons Nominated, and must be published a set number of working days ahead of the actual election date. The number varies based on:

 * *Type of Post* - Parliamentary, Local, devolved Government, etc.
 * *Country* - The United Kingdom has up to four different rules for the same type of election, one for each country.
 * *Calendar* - each country has their own unique set of Bank Holidays.


This library encapsulates timetable legislation for elections run in the United Kingdom and its devolved administrations.

## Usage

```python

from sopn_publish_date import StatementPublishDate
from datetime import date

publish_date = StatementPublishDate()

print(publish_date.national_assembly_for_wales(date(2016, 5, 5)))

# datetime.date(2016, 4, 7)
```

## Documentation

Hosted by readthedocs at [https://sopn-publish-date.readthedocs.io/](https://sopn-publish-date.readthedocs.io/en/latest/overview.html)

## Installation

`pip install sopn_publish_date`
 
## Test

`python -m pytest -v`

## Supported Election Types

 - [x] Local
 - [x] United Kingdom Parliament
 - [x] Scottish Parliament
 - [x] National Assembly for Wales
 - [x] Northern Ireland Assembly
 - [x] Mayoral
 - [x] Mayoral (London)
 - [x] European Parliament
 - [x] Greater London Assembly
 - [x] Police and Crime commissioner