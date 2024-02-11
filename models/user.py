#!/usr/bin/python3
""" This module defines User class"""
from base_model import BaseModel


class User(BaseModel):
    """ User Class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
