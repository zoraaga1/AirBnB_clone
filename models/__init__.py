#!/usr/bin/python3
"""Initialize the application's data model"""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
