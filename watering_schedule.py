#!/usr/bin/env python3

import json
import datetime
from prettytable import PrettyTable
import click


def get_data(filename):
    '''reads the json file and assigns it to a variable'''
    with open(filename) as json_file:
        data = json.load(json_file)
        return data


def water2int(data):
    '''takes the water after key of each plant and turns its value into
    an integer'''
    for plant in data:
        string = plant['water_after']
        day_in_int = string.split(" ")[0]
        plant['water_after'] = day_in_int
    return data


def weekend_fixer(date):
    '''Inspect the date object for saturday or sunday.
    sunday add 24 hours to it if saturday subtract 24 hours from it'''
    if date.weekday() == 5:
        return date - datetime.timedelta(days=1)
    elif date.weekday() == 6:
        return date + datetime.timedelta(days=1)
    return date


def create_schedule(start_date, water_interval, weeks):
    ''' this creates a schedule of days in which watering occurs'''
    # water_interval is an integer
    # weeks is an integer
    result = [start_date]
    end_date = start_date + datetime.timedelta(weeks=weeks)
    next_date = start_date
    while next_date < end_date:
        next_date = result[-1] + datetime.timedelta(days=water_interval)
        result.append(weekend_fixer(next_date))
    return result


def schedule_per_plant(plant_array, start_date, weeks):
    '''Creates a list of dates key value pair for each plant'''
    # start_date is a string
    # weeks is an integer
    for plant in plant_array:
        plant['schedule'] = create_schedule(start_date,
                                            int(plant['water_after']), weeks)
    return plant_array


def add_plant_to_day(start_date, plant_array, weeks):
    '''Takes in the modified plant array that includes a schedule for each plant
    and makes a dictionary with keys of every day in the specified time
    and values as a list of the plants that need to be watered that day'''
    # weeks is an integer
    # start_date is a datetime object
    date_plant_dict = {}
    end_date = start_date + datetime.timedelta(weeks=weeks)
    next_date = start_date
    while next_date < end_date:
        plant_day_arr = []
        for plant in plant_array:
            if next_date in plant['schedule']:
                plant_day_arr.append(plant['name'])
        date_plant_dict[next_date] = plant_day_arr
        next_date += datetime.timedelta(days=1)
    return date_plant_dict


def make_week(date_plant_dict):
    '''This takes the dictionary date_plant_dict and formats it into
    7 day increments so that it's easy to make pretty tables out of it'''
    dates = sorted(date_plant_dict.keys())
    with open("Plant Schedule.txt", 'w') as file_:
        while dates:
            weekly_table = PrettyTable()
            header = []
            plants = []
            for day in dates[:7]:
                header.append(str(day))
                plants.append("\n".join(date_plant_dict[day]))
            dates = dates[7:]
            weekly_table.field_names = header
            weekly_table.add_row(plants)
            file_.write(str(weekly_table) + "\n")


@click.command()
@click.option("--weeks", prompt="Enter number of weeks",
              help="Number of weeks to schedule", type=click.INT, default=12)
@click.option("--start_date", prompt="Starting date as(mm-dd-yyyy)",
              help="Date to begin", type=click.STRING, default="12-16-2019")
def main(weeks, start_date):
    '''This function was made in order to use the click command so that there
    would be a command line prompt. The default for the click is what was
    assigned,being 12 weeks starting from Monday the 16th 2019, but it also
    allows for dynamic starting days and lengths of time'''
    start_date = datetime.datetime.strptime(start_date, '%m-%d-%Y')
    plant_array = schedule_per_plant(water2int(get_data("plant_info.json")),
                                     start_date, weeks)
    make_week(add_plant_to_day(start_date, plant_array, weeks))
    print("Your schedule is now available in 'Plant Schedule.txt'")


if __name__ == "__main__":
    main()
