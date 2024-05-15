#!/usr/bin/python3

import json
import os



class FileStorage:
    """ This class serializes instances to Json file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """ Store a new obj in objects """
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ Save the __objects dictionary """
        with open(self.__file_path, 'w') as file:
            data = {key: value.to_dict()
                    for key, value in self.__objects.items()}
            json.dump(data, file)

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        classes = {"BaseModel": BaseModel}

        return classes

    def reload(self):
        """ load the json file to the __objects dictionary """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}

                self.__objects = obj_dict
        else:
            return
