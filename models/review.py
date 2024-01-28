#!/usr/bin/python3
""" Review module for the HBNB project """
from __future__ import annotations
from typing import TYPE_CHECKING
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


if TYPE_CHECKING:
    from models.place import Place
else:
    Place = "Place"


if TYPE_CHECKING:
    from models.user import User
else:
    User = "User"


class Review(BaseModel, Base):
    """ Review classto store review information """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
