#!/usr/bin/python3
""" This module contains the tests for the FileStorage class. """

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Test cases for the FileStorage class """

    def setUp(self):
        """ Set up the test environment """
        self.file_storage = FileStorage()

    def test_instance(self):
        """ Test for the creation of an instance of FileStorage """
        self.assertIsInstance(self.file_storage, FileStorage)

    def test_all(self):
        """ Test for the all method """
        self.assertIsInstance(self.file_storage.all(), dict)

    def test_new(self):
        """ Test for the new method """
        base_model = BaseModel()
        self.file_storage.new(base_model)
        key = base_model.__class__.__name__ + "." + base_model.id
        self.assertIn(key, self.file_storage.all())

    def test_save(self):
        """ Test for the save method """
        base_model = BaseModel()
        self.file_storage.new(base_model)
        self.file_storage.save()
        with open(self.file_storage._FileStorage__file_path, "r") as file:
            self.assertIn(base_model.__class__.__name__ + "." + base_model.id,
                          file.read())

    def test_reload(self):
        """ Test for the reload method """
        base_model = BaseModel()
        self.file_storage.new(base_model)
        self.file_storage.save()
        self.file_storage.reload()
        key = base_model.__class__.__name__ + "." + base_model.id
        self.assertIn(key, self.file_storage.all())
        self.assertIsInstance(self.file_storage.all()[key], dict)
        self.assertEqual(self.file_storage.all()[key].to_dict(),
                         base_model.to_dict())
        self.assertEqual(self.file_storage.all()[key].created_at,
                         base_model.created_at)
        self.assertEqual(self.file_storage.all()[key].updated_at,
                         base_model.updated_at)
        self.assertEqual(self.file_storage.all()[key].id, base_model.id)
        self.assertEqual(self.file_storage.all()[key].__class__.__name__,
                         base_model.__class__.__name__)

    def test_reload_no_file(self):
        """ Test for the reload method with no file """
        self.file_storage.reload()
        self.assertEqual(self.file_storage.all(), {})

    def test_reload_bad_file(self):
        """ Test for the reload method with a bad file """
        with open(self.file_storage._FileStorage__file_path, "w") as file:
            file.write("This is not a JSON string")
        self.file_storage.reload()
        self.assertEqual(self.file_storage.all(), {})

    def test_reload_empty_file(self):
        """ Test for the reload method with an empty file """
        with open(self.file_storage._FileStorage__file_path, "w") as file:
            file.write("")
        self.file_storage.reload()
        self.assertEqual(self.file_storage.all(), {})

    def test_reload_no_file(self):
        """ Test for the reload method with no file """
        self.file_storage.reload()
        self.assertEqual(self.file_storage.all(), {})
