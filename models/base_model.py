#!/usr/bin/python3

import uuid
from datetime import datetime

"""BaseModel Class"""


class BaseModel():
    """The BaseModel Class, The Project Main Structure"""

    def __init__(self):
        """Constructor Method"""
        # Define a UUID for each instance is created
        self.id = str(uuid.uuid4())
        # Get The Datetime of an instance when its created
        self.created_at = datetime.now()
        # it will be updated every time you change your object
        self.updated_at = datetime.now()

    def __str__(self):
        """String Representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
