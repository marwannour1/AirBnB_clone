""" This module contains the review class for the HBnB project. """

from models.base_model import BaseModel


class Review(BaseModel):
    """ This class contains the review class for the HBnB project. """

    place_id = ""
    user_id = ""
    text = ""
