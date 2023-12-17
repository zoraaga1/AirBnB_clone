#!/usr/bin/python3
"""Test cases"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_city_creation(self):
        city = City()
        self.assertIsInstance(city, City)

    def test_city_attributes(self):
        city = City(name="TestCity", state_id="TestState")
        self.assertEqual(city.name, "TestCity")
        self.assertEqual(city.state_id, "TestState")


if __name__ == '__main__':
    unittest.main()
