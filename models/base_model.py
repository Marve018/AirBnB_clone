#!/usr/bin/python3
"""
    module contains the baseModue class that defines all
    common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime
import models


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
            models.storage.new(self)

    def save(self):
        """
            saves the instance using
            file storage
        """
        from models import storage
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        classDict = self.__dict__.copy()
        classDict['updated_at'] = self.updated_at.isoformat()
        classDict['created_at'] = self.created_at.isoformat()
        classDict['__class__'] = self.__class__.__name__

        return classDict
    
    def __str__(self):
        """
            Return the print/str representation of the BaseModel instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
