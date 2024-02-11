#!user/bin/python3
""" test for review class """
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """ test the review class """

    def test_review(self):
        """ test the review class """
        new = Review()
        self.assertIsInstance(new, "id")
        self.assertIsInstance(new, "created_at")
        self.assertIsInstance(new, "updated_at")
        self.assertIsInstance(new, "place_id")
        self.assertIsInstance(new, "user_id")
        self.assertIsInstance(new, "text")


        """type of the attributes"""
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.place_id, str)
        self.assertIsInstance(new.user_id, str)
        self.assertIsInstance(new.text, str)


if __name__ == "__main__":
    unittest.main()
