#!/usr/bin/python3
"""
Unittest for the BaseModel class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_base_model.py
"""
import unittest
import models
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Declares TestBaseModel Class """
    
    def setUp(self):
        """ class for base test """
        self.filepath = models.storage._FileStorage__file_path
        with open(self.filepath, 'w') as file:
            file.truncate(0)
        models.storage.all().clear()

    def tearDown(self):
        """ class for base test """
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

    def test_basemodel_init(self):
        """ class for base test """
        new = BaseModel()

        """ check if it have methods """
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        
        """ check if it have attributes """
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        
        """ check if it have the correct class """
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime.datetime)
        self.assertIsInstance(new.updated_at, datetime.datetime)
        
if __name__ == '__main__':
    unittest.main()
