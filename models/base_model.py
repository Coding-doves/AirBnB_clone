#!/usr/bin/python3
'''
creating a Base model

'''
import uuid
from datetime import datetime


class BaseModel:
    '''initializing base'''
    unique_id = uuid.uuid4()

    def __init__(self, *args, **kwargs):
        '''public instance'''
        from models import storage

        dt_obj = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, dt_obj)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(BaseModel.unique_id)
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        '''magic method'''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''update datetime with current datetime'''
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''return dictionary - key/value'''
        dic = self.__dict__.copy()

        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()

        return dic
