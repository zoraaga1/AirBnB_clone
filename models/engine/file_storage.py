#!/usr/bin/python3
"""Create FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City 
from models.place import Place
from models.review import Review
from models.state import State

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    Private class attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)"""  # noqa
    """
    Public instance methods:
        all(self)
        new(self, obj)
        def save(self):
        save(self)
        reload(self)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    
    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesnt exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as fi:
                loaded_obj = json.load(fi)
                for key, obj_dict in loaded_obj.items():
                    class_name, obj_id = key.split('.')
                    obj_instance = eval(class_name)(**obj_dict)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass