#!/usr/bin/python3

from basemodel import BaseModel

class User(BaseModel):
    """
    Creating class user that inherits from BaseModel class
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

