#!/usr/bin/python3
from models.base_model import BaseModel
from pathlib import Path
import json
from models.user import User


"""Serialization and Deserialization"""


class FileStorage:
    """Storing Str Repr of Insances to JSON files"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return All objects in objects attr"""
        return FileStorage.__objects

    def new(self, obj):
        """Appending Objects to objects attr"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializing"""

        objects_dict = {}
        for key in FileStorage.__objects.keys():
            objects_dict[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(objects_dict, json_file, indent=4)

    def reload(self):
        """Deserialize"""

        if Path(FileStorage.__file_path).exists():
            with open(FileStorage.__file_path, "r") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                class_name = value["__class__"]
                del value["__class__"]
                FileStorage.__objects[key] = eval(class_name)(**value)

        else:
            return
