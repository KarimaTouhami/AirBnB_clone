#!/usr/bin/python3
"""
Unittest for the BaseModel class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_base_model.py
"""
import unittest
import sys
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Declares TestBaseModel Class """
    new = BaseModel()

    def test_basemodel_init(self):
        """ class for base test """
        new = BaseModel()

        # Check if it have methods
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

        # Check if attributes are created
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))

        """ check if it have the correct class """
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime.datetime)
        self.assertIsInstance(new.updated_at, datetime.datetime)

    def test_basemodel_str(self):
        """ Test string representation of BaseModel """
        new = BaseModel()
        expected_str = f"[{new.__class__.__name__}] ({new.id}) {new.__dict__}"
        self.assertEqual(str(new), expected_str)

    def test_basemodel_save(self):
        """ Test save method of BaseModel """
        new = BaseModel()
        old_updated_at = new.updated_at
        new.save()
        self.assertNotEqual(new.updated_at, old_updated_at)

    def test_basemodel_to_dict(self):
        """ Test to_dict method of BaseModel """
        new = BaseModel()
        new_dict = new.to_dict()

        # Check keys in dictionary
        self.assertIn("id", new_dict)
        self.assertIn("created_at", new_dict)
        self.assertIn("updated_at", new_dict)
        self.assertIn("__class__", new_dict)

        # Check values in dictionary
        self.assertEqual(new_dict["id"], new.id)
        self.assertEqual(new_dict["__class__"], new.__class__.__name__)


if __name__ == '__main__':
    unittest.main()
