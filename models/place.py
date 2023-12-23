#!/usr/bin/python3
""" Place Module for HBNB project """
from __future__ import annotations
from typing import TYPE_CHECKING
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from os import getenv
from models import storage, db_type
from sqlalchemy.orm import relationship


if TYPE_CHECKING:
    from models.city import City
else:
    City = "City"

if TYPE_CHECKING:
    from models.user import User
else:
    User = "User"


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if db_type == "db":
        reviews = relationship("Review", backref="places",
                               cascade="all, delete-orphan")

    else:
        @property
        def reviews(self):
            """ Returns a list of Review instances with
                place_id equals to the current Place.id
            """
            review_objs = [value for key, value in storage.all().items()
                           if "Review" in key and type(self).id in key]
            return review_objs
