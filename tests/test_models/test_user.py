#!/usr/bin/python3
"""Test cases"""


import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        user = User(username="TestUser", email="test@example.com")
        self.assertEqual(user.username, "TestUser")
        self.assertEqual(user.email, "test@example.com")


if __name__ == '__main__':
    unittest.main()
