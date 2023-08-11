#!/usr/bin/python3
'''creating User class that inherits from BaseModel'''
from models import storage
from models.base_model import BaseModel


class User(BaseModel):
    '''user'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
