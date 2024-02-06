import uuid
from datetime import datetime

"""BaseModel Class"""


class BaseModel():
    """The BaseModel Class, The Project Main Structure"""

    def __init__(self):
        """Constructor Method"""
        self.id = str(uuid.uuid4()) #Define a UUID for each instance is created
        self.created_at = datetime.now() #Get The Datetime of an instance when its created
        self.updated_at = datetime.now() #it will be updated every time you change your object

    def __str__(self):
        """String Representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"




