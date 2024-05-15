#!/usr/bin/python3

from models.engine.file_storage import storage
from models.base_model import BaseModel
from user import User

all_objs = storage.all()
print("-- Reloaded objects --")