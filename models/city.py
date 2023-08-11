#!/usr/bin/python3
'''creating City class that inherits from BaseModel'''
from models import storage
from models.base_model import BaseModel


class City(BaseModel):
    '''user'''
    state_id = ""
    name = ""
