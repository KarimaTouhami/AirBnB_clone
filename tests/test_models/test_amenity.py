#!user/bin/python3
"""" test for amenity class """
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """ test the amenity class """

    def test_amenity(self):
        """ test the amenity class """
        new = Amenity()
        self.assertIsInstance(new, "id")
        self.assertIsInstance(new, "created_at")
        self.assertIsInstance(new, "updated_at")
        self.assertIsInstance(new, "name")

        """type of the attributes"""
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.name, str)


if __name__ == "__main__":
    unittest.main()
