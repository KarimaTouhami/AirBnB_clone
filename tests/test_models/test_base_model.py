#!/usr/bin/python3
"""
Unittest for the BaseModel class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_base_model.py
"""
import unittest
import json
import datetime
from unittest.mock import patch
from io import StringIO
import sys
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Declares TestBaseModel Class """

    def setUp(self):
        """ Set up test environment """
        self.assertTruecapture = StringIO()

    def tearDown(self):
        """ Clean up after tests """
        sys.stdout = sys.__stdout__

    def test_basemodel_init(self):
        """ Test BaseModel initialization """
        new = BaseModel()

        # Check if it has methods
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

        # Check if attributes are created
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))

        # Check types of attributes
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime.datetime)
        self.assertIsInstance(new.updated_at, datetime.datetime)

        # Check if object is stored in models.storage
        keyname = "base_model." + new.id
        self.assertTrue(keyname in models.storage.all().keys())
        self.assertTrue(new == models.storage.all()[keyname])

        # Test attribute update
        new.name = "My First Model"
        new.my_number = 89
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(hasattr(new, "my_number"))
        self.assertTrue(hasattr(models.storage.all()[keyname], "name"))
        self.assertTrue(hasattr(models.storage.all()[keyname], "my_number"))

        # Test save method
        old_time = new.updated_at
        new.save()
        self.assertNotEqual(old_time, new.updated_at)
        self.assertGreater(new.updated_at, old_time)

        # Check patch for save method
        with patch('models.storage.save') as mock_save:
            obj = BaseModel()
            new.save()
            mock_save.assert_called_once()

        # Check if it saves in JSON file
        keyname = "BaseModel." + new.id
        with open(models.storage._FileStorage__file_path, 'r') as file:
            saved_json = json.load(file)
        self.assertIn(keyname, saved_json.keys())
        self.assertEqual(saved_json[keyname], new.to_dict())

    def test_basemodel_str(self):
        """ Test string representation of BaseModel """
        new = BaseModel()
        expected_str = f"[{new.__class__.__name__}] ({new.id}) {new.__dict__}"
        self.assertEqual(str(new), expected_str)

    def test_basemodel_init2(self):
        """ Test BaseModel initialization with to_dict """
        new = BaseModel()
        new.name = "John"
        new.my_number = 89
        new2 = BaseModel(**new.to_dict())
        self.assertEqual(new.id, new2.id)
        self.assertEqual(new.name, "John")
        self.assertEqual(new.my_number, 89)
        self.assertEqual(new.to_dict(), new2.to_dict())

    def test_to_dict(self):
        """ Test to_dict method """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model_json = my_model.to_dict()

        expected_keys = ['id', 'created_at', '__class__', 'my_number']
        expected_keys2 = ['updated_at', 'name']
        for key in expected_keys + expected_keys2:
            self.assertIn(key, my_model_json)

        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)
        self.assertEqual(my_model_json['name'], "My_First_Model")
        self.assertEqual(my_model_json['my_number'], 89)

    def test_from_dict(self):
        """ Test from_dict method """
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

    def test_basemodel_init3(self):
        """ Test BaseModel initialization """
        new = BaseModel()
        new2 = BaseModel(new.to_dict())
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)
        self.assertTrue(isinstance(new2.created_at, datetime.datetime))
        self.assertTrue(isinstance(new2.updated_at, datetime.datetime))

        new = BaseModel()

        self.assertEqual(
            str(new),  "[BaseModel] ({}) {}".format(new.id, new.__dict__))

        old_time = new.updated_at
        new.save()
        self.assertGreater(new.updated_at, old_time)


if __name__ == '__main__':
    unittest.main()
