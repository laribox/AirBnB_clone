#!/usr/bin/python3

import json


class FileStorage:
    """ This class serializes instances to Json file"""

    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

class Example:
    name = ""
    def __init__(self):
        self.id = 32

ex = Example()
ex.name = "jin"
print(ex.id)
file = FileStorage()
file.new()
file.save()
print(file.all())
