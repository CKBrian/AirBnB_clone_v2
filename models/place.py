#!/usr/bin/python3
""" Place Module for HBNB project """
from __future__ import annotations
from typing import TYPE_CHECKING
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import getenv
from models import storage
from sqlalchemy.orm import relationship


if TYPE_CHECKING:
    from models.city import City
else:
    City = "City"

if TYPE_CHECKING:
    from models.user import User
else:
    User = "User"

if TYPE_CHECKING:
    from models.amenity import Amenity
else:
    Amenity = "Amenity"

if TYPE_CHECKING:
    from models.review import Review
else:
    Review = "Review"


if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table(
        "place_amenity", Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"),
               primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"),
               primary_key=True, nullable=False)
    )


class Place(BaseModel, Base):
    """ A place to stay """
    if getenv("HBNB_TYPE_STORAGE") == "db":
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

        reviews = relationship("Review", backref="places",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ Returns a list of Review instances with
                place_id equals to the current Place.id
            """
            review_objs = [value for key, value in storage.all().items()
                           if "Review" in key and type(self).id in key]
            return review_objs

        @property
        def amenities(self):
            """ Returns a list of Amenity instances with
                place_id equals to the current Place.id
            """
            return [storage.all()[key] for key in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            self.amenity_ids = [key for key in storage.all(Amenity).keys()
                                if obj.id in key]
