#!/usr/bin/python3
'''creating Review that inherits from BaseModel'''
from models import storage
from models.base_model import BaseModel


class Review(BaseModel):
    '''user'''
    place_id = ""
    user_id = ""
    text = ""
