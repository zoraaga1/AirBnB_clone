#!/usr/bin/python3
"""Test cases"""


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_place_creation(self):
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_attributes(self):
        place = Place(name="TestPlace", city_id="TestCity")
        self.assertEqual(place.name, "TestPlace")
        self.assertEqual(place.city_id, "TestCity")


if __name__ == '__main__':
    unittest.main()
