#!/usr/bin/python3

import uuid
from datetime import datetime
import json
import models

"""BaseModel Class"""


class BaseModel():
    """The BaseModel Class, The Project Main Structure"""

    def __init__(self, *args, **kwargs):
        """Constructor Method"""

        format_time = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, format_time)
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """String Representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the attribute"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Serialize The Object and Modifying attributes"""

        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
