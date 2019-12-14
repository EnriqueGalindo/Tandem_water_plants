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
