#!user/bin/python3
""" test for city class """
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """ test the city class """


    def test_city(self):
        """ test the city class """
        new = City()
        self.assertIsInstance(new, "id")
        self.assertIsInstance(new, "created_at")
        self.assertIsInstance(new, "updated_at")
        self.assertIsInstance(new, "state_id")
        self.assertIsInstance(new, "name")


        """ type of the attributes """
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.state_id, str)
        self.assertIsInstance(new.name, str)


if __name__ == "__main__":
    unittest.main()
