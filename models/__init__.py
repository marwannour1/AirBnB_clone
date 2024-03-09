#!/usr/bin/python3
""" This module creates the storage instance for the application."""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
