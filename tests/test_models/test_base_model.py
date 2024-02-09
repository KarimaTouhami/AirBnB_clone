#!/usr/bin/python3
"""
Unittest for the BaseModel class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_base_model.py
"""
import unittest
import sys
<<<<<<< HEAD
sys.path.append('..')  # Add the parent directory to the sys.path
=======
>>>>>>> origin/main
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
<<<<<<< HEAD
        old_time = new.updated_at
        new.save()
        self.assertNotEqual(old_time, new.updated_at)
        self.assertGreater(new.updated_at, old_time)

    def test_to_dict(self):
        """ Test conversion to dictionary """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model_json = my_model.to_dict()

        expected_keys = ['id', 'created_at', '__class__', 'my_number', 'updated_at', 'name']
        for key in expected_keys:
            self.assertIn(key, my_model_json)

        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)
        self.assertEqual(my_model_json['name'], "My_First_Model")
        self.assertEqual(my_model_json['my_number'], 89)

    def test_from_dict(self):
        """ Test conversion from dictionary """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)

        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)
=======
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
>>>>>>> origin/main


if __name__ == '__main__':
    unittest.main()
