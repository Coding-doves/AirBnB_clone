#!/usr/bin/python3
'''
creating a Base model

'''
import uuid
import datetime


class BaseModel:
    '''initializing base'''
    unique_id = uuid.uuid4()

    def __init__(self):
        '''public instance'''
        self.id = str(BaseModel.unique_id)
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        '''magic method'''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''update datetime with current datetime'''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        '''return dictionary - key/value'''
        dic = self.__dict__.copy()

        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()

        return dic

    def dict_rep(self):
        '''
        dictionary representation with simple object type

        '''
        dic = {
                '__class__': self.__class__.__name__,
                'id': self.id,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat()
                }

        return dic
