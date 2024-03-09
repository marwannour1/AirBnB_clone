#!/usr/bin/python3
""" This file contains the tests for the BaseModel class."""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test cases for the BaseModel class """

    def setUp(self):
        """ Set up the test environment """
        self.base_model = BaseModel()

    def test_instance(self):
        """ Test for the creation of an instance of BaseModel """
        self.assertIsInstance(self.base_model, BaseModel)

    def test_id(self):
        """ Test for the existence of the id attribute """
        self.assertTrue(hasattr(self.base_model, "id"))

    def test_created_at(self):
        """ Test for the existence of the created_at attribute """
        self.assertTrue(hasattr(self.base_model, "created_at"))

    def test_updated_at(self):
        """ Test for the existence of the updated_at attribute """
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def test_str(self):
        """ Test for the __str__ method """
        self.assertEqual(str(self.base_model),
                         "[BaseModel] ({}) {}"
                         .format(self.base_model.id, self.base_model.__dict__))

    def test_save(self):
        """ Test for the save method """
        self.base_model.save()
        self.assertNotEqual(self.base_model.created_at,
                            self.base_model.updated_at)

    def test_to_dict(self):
        """ Test for the to_dict method """
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertEqual(base_model_dict["created_at"],
                         self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict["updated_at"],
                         self.base_model.updated_at.isoformat())
        self.assertEqual(base_model_dict["id"], self.base_model.id)

    def test_kwargs(self):
        """ Test for the creation of an instance with **kwargs """
        base_model_dict = self.base_model.to_dict()
        base_model_copy = BaseModel(**base_model_dict)
        self.assertEqual(self.base_model.to_dict(), base_model_copy.to_dict())

    def test_instance_storage(self):
        """ Test for the existence of the storage attribute """
        self.assertTrue(hasattr(self.base_model, "storage"))

    def test_instance_storage_all(self):
        """ Test for the existence of the storage.all method """
        self.assertTrue(hasattr(self.base_model.storage, "all"))

    def test_instance_storage_new(self):
        """ Test for the existence of the storage.new method """
        self.assertTrue(hasattr(self.base_model.storage, "new"))
