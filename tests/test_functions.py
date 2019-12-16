#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import watering_schedule
import datetime


class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.start_date = datetime.datetime.strptime("12-16-2019", '%m-%d-%Y')
        self.weeks = 12

    def test_no_weekends(self):
        '''checks to make sure that no plants are being watered on a weekend'''
        schedule = watering_schedule.create_plant_array(
            self.weeks, self.start_date
            )
        for plant in schedule:
            for date in sorted(plant['schedule']):
                self.assertNotEqual(date.weekday(), 5)
                self.assertNotEqual(date.weekday(), 6)

    def test_timedeltas(self):
        '''checks to make sure that the distance between waterings for any given plant
        is no more or less than one day from its desired watering interval'''
        schedule = watering_schedule.create_plant_array(
            self.weeks, self.start_date
            )
        for plant in schedule:
            date_list = plant['schedule']
            delta = datetime.timedelta(days=plant['water_after'])
            prev_day = date_list[0]
            for date in date_list[1:]:
                self.assertTrue(
                    date - prev_day >= delta - watering_schedule.one_day
                    )
                self.assertTrue(
                    date - prev_day <= delta + watering_schedule.one_day
                    )
                prev_day = date

    def test_twelve_weeks(self):
        schedule = watering_schedule.create_plant_array(
            self.weeks, self.start_date
            )
        for plant in schedule:
            date_list = plant['schedule']
            total_days = date_list[-1] - date_list[0]
            weeks = total_days.days / 7.0
            self.assertGreaterEqual(weeks, self.weeks - 1)
