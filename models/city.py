#!/usr/bin/python3
""" A class names city that inherits from Basemodel """

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city"""
    state_id = ""
    name = ""

    def name(self):
        return self._name

    def name(self, value):
        if value is not None:
            self._name = value
        else:
            raise ValueError("name cannot be None")

    def state_id(self):
        return self._state_id

    def state_id(self, value):
        if value is not None:
            self._state_id = value
        else:
            raise ValueError("state_id cannot be None")
