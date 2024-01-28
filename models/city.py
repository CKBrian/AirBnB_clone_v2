#!/usr/bin/python3
""" City Module for HBNB project """
from __future__ import annotations
from typing import TYPE_CHECKING
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


if TYPE_CHECKING:
    from models.state import State
else:
    State = "State"

if TYPE_CHECKING:
    from models.place import Place
else:
    Place = "Place"


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="city",
                              cascade="all, delete-orphan")
    else:
        state_id = ""
        name = ""
