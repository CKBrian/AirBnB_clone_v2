#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv


# load environment variable
db_type = getenv("HBNB_TYPE_STORAGE")

# Switch between FileStorage and DBStorage engines
if db_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
