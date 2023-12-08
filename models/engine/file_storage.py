#!/usr/bin/python3
"""
    module contains the FileStorage class that serializes
    instances to a JSON file and deserializes JSON file to instances
"""
import json
from os import path
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
        class FileStorage where serializes
        instances to a JSON
        file and deserializes JSON file to instances:
    """
    def __init__(self):
        """
            initializer
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
            returns the dictionary __objects
        """
        return self.__objects
    
    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
            serializes __objects to the JSON file
        """
        objD = {}
        with open(self.__file_path, "w", encoding="utf-8") as fjson:
            for key, value in self.__objects.items():
                objD[key] = value.to_dict()
            fjson.write(json.dumps(objD))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as fjson:
                data = json.load(fjson)
                for key in data.values():
                    cls_name = key["__class__"]
                    del key["__class__"]
                    self.new(eval(cls_name)(**key))
        except FileNotFoundError:
            return
