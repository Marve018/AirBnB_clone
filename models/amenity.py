#!/usr/bin/python3
"""
    module contains the amenity class that
    inherits from the BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        class inherits from baseModel
        Public class attributes:
            name: string - empty string
    """
    name = ""
