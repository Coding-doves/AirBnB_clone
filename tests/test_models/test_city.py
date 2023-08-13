#!/usr/bin/python3
'''testcase for city class'''
import unittest
import datetime
from models.city import City


class TestCity(unittest.TestCase):
    '''
    Test cases for the City class.

    '''
    def test_city(self):
        '''testing'''
        self.city = City()
        self.assertIsInstance(self.city.created_at, datetime.datetime)
        self.assertIsInstance(self.city.updated_at, datetime.datetime)

        self.city.name = 'Ada'
        self.assertEqual(self.city.name, 'Ada')

        self.city.state_id = '3456'
        self.assertEqual(self.city.state_id, '3456')

        prev_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(prev_updated_at, self.city.updated_at)

        json_model = self.city.to_dict()
        self.assertIsInstance(json_model, dict)
        self.assertIn('__class__', json_model)
        self.assertEqual(json_model['__class__'], 'City')
        self.assertIsInstance(json_model['state_id'], str)
        self.assertEqual(json_model['name'], 'Ada')
        self.assertIsInstance(json_model['created_at'], str)
        self.assertIsInstance(json_model['updated_at'], str)

    def test_city_with_kwargs(self):
        '''testing'''
        date = datetime.datetime.today()
        dt_frmt = date.isoformat()
        city = City(
                state_id="345",
                name='George',
                created_at=dt_frmt,
                updated_at=dt_frmt
                )
        self.assertEqual(city.state_id, "345")
        self.assertEqual(city.name, "George")
        self.assertEqual(city.created_at, date)
        self.assertEqual(city.updated_at, date)

    def test_city_with_none_kwargs(self):
        '''testing'''
        with self.assertRaises(TypeError):
            City(
                    id=None,
                    name='',
                    state_id='',
                    created_at=None,
                    updated_at=None
                    )


        if __name__ == '__main__':
            unittest.main()
