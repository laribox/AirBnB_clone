#!/usr/bin/python3
"""Creating class user that inherits from BaseModel class"""
from models.basemodel import BaseModel

class User(BaseModel):
    """
    User class
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

