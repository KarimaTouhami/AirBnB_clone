#!user/bin/python3
""" This module defines Review class """
from base_model import BaseModel


class Review(BaseModel):
    """ Review Class """
    place_id = ""
    user_id = ""
    text = ""
