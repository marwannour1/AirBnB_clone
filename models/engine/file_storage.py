#!/usr/bin/python3
""" This module contains the storage class for the file storage engine. """

import json


class FileStorage:
    """ This class serializes instances to a JSON file and deserializes JSON"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        with open(self.__file_path, "w") as file:
            my_dict = {}
            for key, value in self.__objects.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r") as file:
                from models.base_model import BaseModel
                from models.user import User
                my_dict = json.load(file)
                for key, value in my_dict.items():
                    if value["__class__"] == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    elif value["__class__"] == "User":
                        self.__objects[key] = User(**value)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
