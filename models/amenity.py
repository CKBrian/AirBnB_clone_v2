#!/usr/bin/python3
""" State Module for HBNB project """
from __future__ import annotations
from typing import TYPE_CHECKING
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


if TYPE_CHECKING:
    from models.place import Place
else:
    Place = "Place"


class Amenity(BaseModel, Base):
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       back_populates="amenities")
    else:
        name = ""
