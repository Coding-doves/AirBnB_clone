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

        with open(FileStorage.__file_path, 'w', encoding='utf8') as file:
            json.dump(obj, file)

    def reload(self):
        '''
        deserializes the JSON file to __objects

        '''
        try:
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review
            classes = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review
            }

            with open(FileStorage.__file_path, 'r', encoding='utf8') as file:
                objt = json.load(file)

                for key, val in objt.items():
                    cls_name, obj_id = key.split('.')
                    cls = classes.get(cls_name)

                if cls:
                    inst = cls(**val)
                    FileStorage.__objects[key] = inst
        except FileNotFoundError:
            pass
