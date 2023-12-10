#!/usr/bin/python3
"""Test cases"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_state_creation(self):
        state = State()
        self.assertIsInstance(state, State)

    def test_state_attributes(self):
        state = State(name="TestState")
        self.assertEqual(state.name, "TestState")


if __name__ == '__main__':
    unittest.main()
