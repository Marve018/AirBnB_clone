#!/usr/bin/python3
"""
    A class that defines the user and 
    inherits from the BaseModel
"""

from models.base_model import BaseModel

class User(BaseModel):
    """Representing the user class and its properties
        ALL pointing to empty strings
        props:
            Email: Represents the users email
            Password: Represents the users password
            first_name: Users first name
            last_name: Users last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
