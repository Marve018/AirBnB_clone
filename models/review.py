#!/usr/bin/python3
"""
    module contains the review class that
    inherits from the BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        class inherits from baseModel
        Public class attributes:
            place_id: string - empty string: it will be the Place.id
            user_id: string - empty string: it will be the User.id
            text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
