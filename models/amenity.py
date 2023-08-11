#!/usr/bin/python3
'''creating Amenity class that inherits from BaseModel'''
from models import storage
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''user'''
    name = ""
