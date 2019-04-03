# sopn-publish-date

[![Build Status](https://travis-ci.org/mrwilson/sopn-publish-date.svg?branch=master)](https://travis-ci.org/mrwilson/sopn-publish-date)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Documentation Status](https://readthedocs.org/projects/sopn-publish-date/badge/?version=latest)](https://sopn-publish-date.readthedocs.io/en/latest/overview.html?badge=latest)
> Given the polling day of an election in the UK, when should the Statement of Persons Nominated (SoPN) be published?

## Test

`python -m pytest -v`

## Sources

The [bank holidays JSON](./sopn_publish_date/bank-holidays.json) is provided by [gov.uk](https://www.gov.uk/bank-holidays.json) under the [Open Government Licence](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)

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

## Useful Links (delete pre-1.0)

 * Association of Electoral Administrators [review of May 2016 elections](https://www.aea-elections.co.uk/wp-content/uploads/2016/09/aea-rep-2016-pushed-to-the-absolute-limit-the-electoral-year-never-to-forget-with-links.pdf) (Appendix D contains full timetabling for all concurrent elections)
 * TheyWorkForYou/Hansard: Lord Roberts of Llandudno on [overseas voting](https://www.theyworkforyou.com/lords/?id=2011-03-02a.1127.0)
 
## Relevant Legislation

 * **UK Parliament** - https://www.legislation.gov.uk/ukpga/1983/2/contents (Schedule 1, rules 1 & 2), two amendments outstanding: https://www.legislation.gov.uk/ukpga/2011/14 and https://www.legislation.gov.uk/ukpga/2013/6/section/14
 
 * **Northern Ireland Assembly** - https://www.legislation.gov.uk/uksi/2009/256/made (Schedule 1)
 
 * **Scottish Parliament** - https://www.legislation.gov.uk/ssi/2015/425/made (Schedule 2, rules 1 & 2)
 
 * **Welsh Assembly/Senedd** - https://www.legislation.gov.uk/uksi/2007/236/made (Schedule 5, rules 1 & 2), amended by https://www.legislation.gov.uk/uksi/2016/272/article/18/made
 
 * **Greater London Authority** - https://www.legislation.gov.uk/uksi/2007/3541/made (Rule 7 and Schedules 1/2/3/5/6/7, rules 3 & 4), amended by https://www.legislation.gov.uk/uksi/2016/24/article/6/made
 
 * **Police & Crime Commissioner** - https://www.legislation.gov.uk/uksi/2012/1917/made (Schedule 3, rules 1 & 3), amended by https://www.legislation.gov.uk/uksi/2014/921/article/31/made
 and https://www.legislation.gov.uk/uksi/2016/300/article/11/made
 
 * **Combined Authority Mayors** - https://www.legislation.gov.uk/uksi/2017/67/made (Schedules 1/3, rules 3 & 4)
 
 * **Local (Principal Areas), England & Wales** - https://www.legislation.gov.uk/uksi/2006/3304/made (Schedules 2/3, rules 1 & 2), amended by https://www.legislation.gov.uk/uksi/2014/494/made (Rules 3(2) and 4(2))
 
 * **Local Mayors, England & Wales** - https://www.legislation.gov.uk/uksi/2007/1024/made (Schedules 1/3, rules 3 & 4), amended by https://www.legislation.gov.uk/uksi/2014/370/made (Regulations 5(2) and 7(2))
 
 * **Parishes & Communities, England & Wales** - https://www.legislation.gov.uk/uksi/2006/3305/made (Schedules 2/3, rules 1 & 2), amended by https://www.legislation.gov.uk/uksi/2014/492/made (Rules 3(2) and 4(2))
 
 * **Local, Northern Ireland** - https://www.legislation.gov.uk/apni/1962/14 (Schedule 5, rules 1 & 2), amended by https://www.legislation.gov.uk/uksi/2010/2977/schedule/1/part/4/made
 
 * **Local, Scotland** - https://www.legislation.gov.uk/ssi/2011/399/made (Schedule 1, rules 1 & 2)
 
 * **City of London** - Section 10(1) of the Act of Common Council of 14 July 1960 (as substituted by section 6 of the Act of Common Council of 6 November 2008)
 (source: https://www.cityoflondon.gov.uk/about-the-city/voting-elections/Documents/wardmote-book-june-2014.pdf (Section 4, paragraph 20))
 
 * **European Parliament** - https://www.legislation.gov.uk/uksi/2009/186/made (Schedule 2, rules 1 & 2)
 
 