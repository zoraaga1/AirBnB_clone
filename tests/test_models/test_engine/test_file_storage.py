#!/usr/bin/python3
"""Test cases"""


import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_file_storage_all(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_file_storage_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_file_storage_save_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, new_storage.all())


if __name__ == '__main__':
    unittest.main()
