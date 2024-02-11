#!user/bin/python3
""" test for state class """
import unittest
from models.state import State
from datetime import datetime


class StateTest(unittest.TestCase):
    """ class to test State class """

    def test_state(self):
        """ test State class """
        new = State()
        self.assertIsInstance(new, "id")
        self.assertIsInstance(new, "created_at")
        self.assertIsInstance(new, "updated_at")
        self.assertIsInstance(new, "name")

        """ check if it have the correct class """
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.name, str)


if __name__ == "__main__":
    unittest.main()
