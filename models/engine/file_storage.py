#!/usr/bin/python3
'''
serializes instances to a JSON file and deserializes JSON file to instances

'''
import json


class FileStorage:
    '''serialize and deserialize'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''
        set in __objects the obj with key <obj class name>.id

        '''
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        serializes __objects to the JSON file (path: __file_path)

        '''
        obj = {}
        for key, val in FileStorage.__objects.items():
            obj[key] = val.to_dict()

        with open(self.__file_path, 'w', encoding='utf8') as file:
            string = json.dumps(obj)
            file.write(string)

    def reload(self):
        '''
        deserializes the JSON file to __objects

        '''
        try:
            with open(self.__file_path, 'r', encoding='utf8') as file:
                objt_file = file.read()

                from models.base_model import BaseModel

                if objt_file:
                    objt = json.loads(objt_file)
                    for key, val in objt.items():
                        cls_nam, obj_id = key.split('.')

                        instance = BaseModel(**val)
                        self.__objects[key] = instance
        except FileNotFoundError:
            pass
