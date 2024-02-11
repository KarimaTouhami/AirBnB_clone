#!user/bin/python3
""" unit test for Place class """
import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """ class to test Place class """

    def test_place(self):
        """ test Place class """
        new = Place()
        self.assertIsInstance(new, "id")
        self.assertIsInstance(new, "created_at")
        self.assertIsInstance(new, "updated_at")
        self.assertIsInstance(new, "city_id")
        self.assertIsInstance(new, "user_id")
        self.assertIsInstance(new, "name")
        self.assertIsInstance(new, "description")
        self.assertIsInstance(new, "number_rooms")
        self.assertIsInstance(new, "number_bathrooms")
        self.assertIsInstance(new, "max_guest")
        self.assertIsInstance(new, "price_by_night")
        self.assertIsInstance(new, "latitude")
        self.assertIsInstance(new, "longitude")
        self.assertIsInstance(new, "amenity_ids")

        """ check if it have the correct class """
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.city_id, str)
        self.assertIsInstance(new.user_id, str)
        self.assertIsInstance(new.name, str)
        self.assertIsInstance(new.description, str)
        self.assertIsInstance(new.number_rooms, int)
        self.assertIsInstance(new.number_bathrooms, int)
        self.assertIsInstance(new.max_guest, int)
        self.assertIsInstance(new.price_by_night, int)
        self.assertIsInstance(new.latitude, float)
        self.assertIsInstance(new.longitude, float)
        self.assertIsInstance(new.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
