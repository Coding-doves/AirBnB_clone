#!/usr/bin/python3
'''testcase for base class'''

import unittest
import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModal(unittest.TestCase):
    '''
    Test cases for the Base class.
    '''
    def test_base_model(self):
        '''testing base'''
        self.base = BaseModel()
        '''self.assertIsInstance(self.base.id, uuid.uuid4)'''
        self.assertIsInstance(self.base.created_at, datetime.datetime)
        self.assertIsInstance(self.base.updated_at, datetime.datetime)

        self.base.name = 'Model Airbnb'
        self.assertEqual(self.base.name, 'Model Airbnb')

        self.base.my_number = 20
        self.assertEqual(self.base.my_number, 20)

        prev_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(prev_updated_at, self.base.updated_at)

        json_model = self.base.to_dict()
        self.assertIsInstance(json_model, dict)
        self.assertIn('__class__', json_model)
        self.assertEqual(json_model['__class__'], 'BaseModel')
        self.assertIsInstance(json_model['id'], str)
        self.assertEqual(json_model['my_number'], 20)
        self.assertEqual(json_model['name'], 'Model Airbnb')
        self.assertIsInstance(json_model['created_at'], str)
        self.assertIsInstance(json_model['updated_at'], str)

        dic = {
             '__class__': 'BaseModel',
             'id': uuid.uuid4(),
             'name': 'Model Airbnb',
             'my_number': 20,
             'created_at': self.base.created_at,
             'updated_at': self.base.updated_at
        }
        dictionary = BaseModel
        model = dictionary.dict_rep(dic)
        self.assertEqual(model, 'BaseModel')
        self.assertIsInstance(model.id, uuid.uuid4)
        self.assertEqual(json_model.my_number, 20)
        self.assertEqual(json_model.name, 'Model Airbnb')
        self.assertIsInstance(model.created_at, datetime.datetime)
        self.assertIsInstance(model.updated_at, datetime.datetime)

        if __name__ == '__main__':
            unittest.main()
