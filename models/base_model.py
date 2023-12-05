#!/usr/bin/python3
"""
    module contains the baseModue class that defines all
    common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime



class BaseModel:
    """
        Class BaseModel
        defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
            class initializer
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """
            updates the instance attribute
            updated_at with the current datetime
        """
        updated_at = datetime.now()


