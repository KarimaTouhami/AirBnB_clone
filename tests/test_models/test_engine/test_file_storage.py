#!user/bin/python3
""" Unittest for the FileStorage class """
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """ Declares TestFileStorage Class """

    def test_doc(self):
        """ classes and methods documentation """

        self.assertIsNotNone(models.engine.file_storage.FileStorage.__doc__)
        self.assertIsNotNone(models.engine.file_storage.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.all.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.new.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.save.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.reload.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.__init__.__doc__)

    def test_class(self):
        """ Test class type """

        self.assertIsInstance(models.engine.file_storage.FileStorage(),
                              models.engine.file_storage.FileStorage)

    def test_all(self):
        """check if all method is working"""

        self.assertIsNotNone(models.engine.file_storage.FileStorage().all)

    def test_new(self):
        """check if new method is working"""

        self.assertIsNotNone(models.engine.file_storage.FileStorage().new)

    def test_save(self):
        """check if save method is working"""

        self.assertIsNotNone(models.engine.file_storage.FileStorage().save)

    def test_reload(self):
        """check if reload method is working"""

        self.assertIsNotNone(models.engine.file_storage.FileStorage().reload)

    def test_all_method(self):
        """check if all method is working"""

        self.assertIsNotNone(models.engine.file_storage.FileStorage().all())

    def test_models_all(self):
        """check if all method is working"""

        self.assertIsNotNone(models.storage.all())


if __name__ == '__main__':
    unittest.main()
