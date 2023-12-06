#!/usr/bin/python3
"""
    module contains the FileStorage class that serializes
    instances to a JSON file and deserializes JSON file to instances
"""
import json
import os
import models


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

    
