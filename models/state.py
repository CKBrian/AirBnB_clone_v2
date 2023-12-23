#!/usr/bin/python3
""" State Module for HBNB project """
from __future__ import annotations
from typing import TYPE_CHECKING
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import db_type


if TYPE_CHECKING:
    from models.city import City
else:
    City = "City"


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    if db_type != "db":
        @property
        def cities(self):
            """Gets the states id"""
            from models.engine import FileStorage
            curr_objs = FileStorage.all()
            city_list = [value for key, value in curr_objs
                         if self.id in key and "City" in key]
            return city_list
