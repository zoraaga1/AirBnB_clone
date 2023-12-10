#!/usr/bin/python3
"""Test cases"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_amenity_creation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_attributes(self):
        amenity = Amenity(name="TestAmenity")
        self.assertEqual(amenity.name, "TestAmenity")


if __name__ == '__main__':
    unittest.main()
