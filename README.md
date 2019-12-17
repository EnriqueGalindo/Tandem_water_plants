![LOGO](happy_flower.jpeg)
# Watering Schedule Maker
> A take home programming challenge for Tandem Chicago

An application that generates a watering schedule for the next 12 weeks for all of the plants starting next Monday, December 16th, 2019.

## Quickstart

`$ pip install pipenv`

`$ git clone https://github.com/EnriqueGalindo/Tandem_water_plants.git`

`$ cd Tandem_water_plants`

`$ Tandem_water_plants git:(master) pipenv install`

`$ Tandem_water_plants git:(master) pipenv run python watering_schedule.py`
```
+-------------------+------------+------------+-------------------+------------+------------+------------+
|     12-16-2019    | 12-17-2019 | 12-18-2019 |     12-19-2019    | 12-20-2019 | 12-21-2019 | 12-22-2019 |
+-------------------+------------+------------+-------------------+------------+------------+------------+
|  Fiddle Leaf Fig  |            | Wavy Fern  |  Bird's Nest Fern | Wavy Fern  |            |            |
|    Snake Plant    |            |            | Bell Pepper Plant |            |            |            |
|     Money Tree    |            |            |  Strawberry Plant |            |            |            |
|  Bird's Nest Fern |            |            |                   |            |            |            |
|       Croton      |            |            |                   |            |            |            |
| Bell Pepper Plant |            |            |                   |            |            |            |
```

## Features

* The user can view which plant(s) to water on which date(s).
* The schedule covers the next 12 weeks starting next Monday, with the assumption that next Monday is December
 16th, 2019.
* No plants are watered on Saturdays or Sundays.
* Each plant is watered on its desired schedule or as close as possible, taking into account weekends.
* Built out in a python virtual environment so that it is ready to go upon cloning
* Uses a virtual environment to prevent the need to download various libraries

## Installing / Getting started

`$ git clone https://github.com/EnriqueGalindo/Tandem_water_plants.git`

`$ cd Tandem_water_plants`

`$ Tandem_water_plants git:(master) pipenv install`

`$ Tandem_water_plants git:(master) pipenv run python watering_schedule.py`
```
Enter number of weeks [12]: 
```
You may enter any number of weeks, but the default, if nothing is entered, is 12.
```
Starting date as(mm-dd-yyyy) [12-16-2019]: 
```
You may enter any date in the form of mm-dd-yyyy, but the default, if nothing is entered, 12-16-2019
```
Your schedule is now available in 'watering_schedule.txt'
```

### Initial Configuration

you will need python3 installed
you will need to have pipenv installed 
`pip install pipenv`

### Next Steps

Given more time I would have liked to use the library holidays from datetime which is a "fast, efficient Python 
library for generating country, province and state specific sets of holidays on the fly. It aims to make 
determining whether a specific date is a holiday as fast and flexible as possible." ([pypi.org](https://pypi.org/project/holidays/)) 
In this way I would be able to allow the schedule to be more flexible as I expect people will
not be around to water plants on holidays.

I would also have liked to make the testing more robust. Currently, the tests check for the acceptance criterea,
and, in doing so they, they check the major functionality of the various functions used throughout the program. 
However, nothing is currently written to test edge cases, and nothing is written to test each function individually.
