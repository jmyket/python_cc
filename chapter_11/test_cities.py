import unittest
from chapter_11.city_functions import city_location

class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_loc(self):
        """Do cities such as 'London, England' work?"""
        city_loc = city_location('london', 'england')
        self.assertEqual(city_loc, "London, England")

    def test_city_loc_pop(self):
        """Do entries such as 'London, England - population 8982000' work?'"""
        city_loc_pop = city_location('london', 'england', 8_982_000)
        self.assertEqual(city_loc_pop, "London, England - population 8982000")

if __name__ == '__main__':
    unittest.main()