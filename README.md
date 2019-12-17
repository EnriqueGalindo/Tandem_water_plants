# Watering Schedule Maker
> A take home programming challenge for Tandem Chicago

An application that generates a watering schedule for the next 12 weeks for all of the plants starting next Monday, December 16th, 2019.

## Installing / Getting started

`<$ git clone https://github.com/EnriqueGalindo/Tandem_water_plants.git>`
```
Cloning into 'Tandem_water_plants'...
remote: Enumerating objects: 39, done.
remote: Counting objects: 100% (39/39), done.
remote: Compressing objects: 100% (30/30), done.
remote: Total 39 (delta 16), reused 29 (delta 6), pack-reused 0
Unpacking objects: 100% (39/39), done.
```
`<$ cd Tandem_water_plants >`

`<Tandem_water_plants git:(master) $ pipenv install>`
```
Creating a virtualenv for this project…
Pipfile: /Users/user/Projects/Tandem_water_plants/Pipfile
Using /usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/bin/python3.7m (3.7.4) to create virtualenv…
⠹Running virtualenv with interpreter /usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/bin/python3.7m
Using base prefix '/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7'
New python executable in /Users/username/Projects/Tandem_water_plants/.venv/bin/python3.7
Also creating executable in /Users/username/Projects/Tandem_water_plants/.venv/bin/python
Installing setuptools, pip, wheel...
done.
Virtualenv location: /Users/user/Projects/Tandem_water_plants/.venv
Installing dependencies from Pipfile.lock (a1cb5a)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 2/2 — 00:00:02
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```
`<Tandem_water_plants git:(master) $ pipenv run python watering_schedule.py>`
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
`<pip install pipenv>`

## Features

* The user can view which plant(s) to water on which date(s).
* The schedule covers the next 12 weeks starting next Monday, with the assumption that next Monday is December
 16th, 2019.
* No plants are watered on Saturdays or Sundays.
* Each plant is watered on its desired schedule or as close as possible, taking into account weekends.
* Built out in a python virtual environment so that it is ready to go upon cloning
* Uses a virtual environment to prevent the need to download various libraries

### Next Steps

Given more time I would have liked to use the library holidays from datetime which is a "fast, efficient Python 
library for generating country, province and state specific sets of holidays on the fly. It aims to make 
determining whether a specific date is a holiday as fast and flexible as possible." ([pypi.org](https://pypi.org/project/holidays/)) 
In this way I would be able to allow the schedule to be more flexible as I expect people will
not be around to water plants on holidays.

I would also have liked to make the testing more robust. Currently, the tests check for the acceptance criterea,
and, in doing so they, they check the major functionality of the various functions used throughout the program. 
However, nothing is currently written to test edge cases, and nothing is written to test each function individually.


### Deploying / Publishing

clone the repo
