#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
     """
    This is a base model class for our program.
    defines all common attributes/methods for other classes.
    """
    def __init__(self):
         """
        Constructor method for BaseModel.
        Initializes a new instance of BaseModel with the given name.
        """
        self.id = str(uuid.uuid4())  # Generate a unique ID for each instance
        self.created_at = datetime.now()  # Assign current datetime when instance is created
        self.updated_at = datetime.now()  # Assign current datetime when instance is created

    def __str__(self):
        """Returns a string representation of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates time by saving new current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns data in the dictionary (currently time created and time updated)"""
        obj_dict = self.__dict__.copy()
        """Using obj_dict to arrange the tuple and process the data that is in JSON"""
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict