#!/usr/bin/python3
""" State Module for HBNB project """
from __future__ import annotations
from typing import TYPE_CHECKING
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


if TYPE_CHECKING:
    from models.city import City
else:
    City = "City"

if TYPE_CHECKING:
    from models.engine import FileStorage
else:
    FileStorage = "FileStorage"


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """Gets the states id"""
            from models.city import City
            from models.engine.file_storage import FileStorage
            curr_objs = FileStorage.all(City)
            city_list = [value for key, value in curr_objs.items()
                         if "City" in key and
                         self.id == value.to_dict().get('state_id')]
            return city_list
