#!/usr/bin/python3

""" Base Model Module representing the base class for all models"""


import uuid
from datetime import datetime


class BaseModel:
    """ Base Model Class """

    def __init__(self):
        """ Constructor for BaseModel class """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ String representation of BaseModel class """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at with the current
        datetime """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the
        instance """

        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()

        return dict_copy
