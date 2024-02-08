#!/usr/bin/python3

import uuid
from datetime import datetime
import json

"""BaseModel Class"""


class BaseModel():
    """The BaseModel Class, The Project Main Structure"""

    def __init__(self):
        """Constructor Method"""
        # Define a UUID for each instance is created
        self.id = str(uuid.uuid4())
        # Get The Datetime of an instance when its created
        self.created_at = datetime.today()
        # it will be updated every time you change your object
        self.updated_at = datetime.today()

    def __str__(self):
        """String Representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the attribute"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Serialize The Object and Modifying attributes"""

        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
