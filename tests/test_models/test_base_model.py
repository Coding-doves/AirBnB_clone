#!/usr/bin/python3
'''testcase for base class'''

import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModal(unittest.TestCase):
    '''
    Test cases for the Base class.
    '''
    def test_base_model(self):
        '''testing base'''
        self.base = BaseModel()
        self.assertIsInstance(self.base.id, str)
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

    def test_base_model_with_kwargs(self):
        '''testing'''
        date = datetime.datetime.today()
        dt_frmt = date.isoformat()
        basemodel = BaseModel(id="345", created_at=dt_frmt, updated_at=dt_frmt)
        self.assertEqual(basemodel.id, "345")
        self.assertEqual(basemodel.created_at, date)
        self.assertEqual(basemodel.updated_at, date)

    def test_base_model_with_none_kwargs(self):
        '''testing'''
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


        if __name__ == '__main__':
            unittest.main()
