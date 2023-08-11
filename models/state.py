#!/usr/bin/python3
'''creating State class that inherits from BaseModel'''
from models import storage
from models.base_model import BaseModel


class State(BaseModel):
    '''user'''
    name = ""
