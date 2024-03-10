#!/usr/bin/python3
""" This module contains the user class for the HBnB project. """

from models.base_model import BaseModel


class User(BaseModel):
    """ This class contains the user class for the HBnB project. """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
