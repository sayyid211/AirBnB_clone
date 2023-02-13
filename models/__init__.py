#!/usr/bin/python3

"""
Create file storage system for airbnb
"""

from models.engine.file_storage import FileStorage


store = FileStorage()
storage.reload()
