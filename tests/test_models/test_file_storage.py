#!/usr/bin/python3
'''testcase for base class'''

import unittest
import datetime
import uuid
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    '''
    Test cases for the Base class.

    '''
    def test_file_storage(self):
        '''testing file_storage'''
        self.base = BaseModel()
        self.base.name = "Model Airbnb"
        self.base.my_number = 20
        '''save BaseModel to storage'''
        self.base.save()

        self.assertIsInstance(self.base.created_at, datetime.datetime)
        self.assertIsInstance(self.base.updated_at, datetime.datetime)
        self.assertEqual(self.base.name, 'Model Airbnb')
        self.assertEqual(self.base.my_number, 20)

        '''testing save method''
        key = f"{self.base.__class__.__name__}.{self.base.id}"
        storage.save()
        with open(storage.__file_path, 'r', encoding='utf8') as file:
            json_data = file.read()
            self.assertIn(key, json_data)

        ''clears objects in storage making it empty''
        storage.__objects = {}

        ''create new instance''
        new_base = BaseModel()
        new_base.save()
        key = f"{new_base.__class__.__name__}.{new_base.id}"
        self.assertIn(key, storage.__objects)
        self.assertEqual(storage.__objects[key], new_base)''


        ''clears objects in storage making it empty''
        storage.__objects = {}

        ''clears objects in storage and reload''
        storage.reload()

        self.assertIn(key, storage.__objects)
        self.assertEqual(storage.__objects[key].id, self.base.id)
    '''
    if __name__ == '__main__':
        unittest.main()
