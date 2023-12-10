#!/usr/bin/python3
"""Test cases"""


#!/usr/bin/python3
"""Test cases"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_review_creation(self):
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_attributes(self):
        review = Review(text="TestReview", user_id="TestUser")
        self.assertEqual(review.text, "TestReview")
        self.assertEqual(review.user_id, "TestUser")

    # Add more test cases for Review methods as needed

if __name__ == '__main__':
    unittest.main()
