import unittest
import watering_schedule
import datetime


class TestFunctions(unittest.TestCase):
    def test_no_weekends(self):
        '''checks to make sure that no plants are being watered on a weekend'''
        start_date = datetime.datetime.strptime("12-16-2019", '%m-%d-%Y')
        weeks = 12
        data = watering_schedule.get_data("plant_info.json")
        plant_array = watering_schedule.water2int(data)
        plant_w_schedule = watering_schedule.schedule_per_plant(start_date,
                                                                weeks,
                                                                plant_array)
        for plant in plant_w_schedule:
            for date in sorted(plant['schedule']):
                if date.weekday() == 6 or date.weekday() == 5:
                    self.assertRaises(TypeError)

    def test_timedeltas(self):
        '''checks to make sure that the distance between waterings for any given plant
        is no more or less than one day from its desired watering interval'''
        start_date = datetime.datetime.strptime("12-16-2019", '%m-%d-%Y')
        weeks = 12
        old_day
        data = watering_schedule.get_data("plant_info.json")
        plant_array = watering_schedule.water2int(data)
        plant_w_schedule = watering_schedule.schedule_per_plant(start_date,
                                                                weeks,
                                                                plant_array)
        for plant in plant_w_schedule:
            while sorted(plant['schedule']):
                new_day = sorted(plant['schedule']).pop()
                if old_day == 0:
                    old_day = new_day
                    continue
                self.assertTrue(new_day - old_day >= datetime.timedelta(
                                days=int(plant['water_after']) - 1)
                self.assertTrue(new_day - old_day <= datetime.timedelta(
                                days=int(plant['water_after']) + 1)
                old_day = new_day
