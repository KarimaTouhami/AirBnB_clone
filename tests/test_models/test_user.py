#!user/bin/python3
""" Unit test for User class"""
import unittest
from models.user import User
import datetime


class Test_User(unittest.TestCase):
    """ class to test User class """
    
    def test_user(self):
        """ test User class """
        new = User()
        self.assertIsInstance(new, "id")
        self.assertIsInstance(new, "created_at")
        self.assertIsInstance(new, "updated_at")
        self.assertIsInstance(new, "email")
        self.assertIsInstance(new, "password")
        self.assertIsInstance(new, "first_name")
        self.assertIsInstance(new, "last_name")
        
        """ check if it have the correct class """
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.email, str)
        self.assertIsInstance(new.password, str)
        self.assertIsInstance(new.first_name, str)
        self.assertIsInstance(new.last_name, str)
        
        
if __name__ == "__main__":
    unittest.main()
