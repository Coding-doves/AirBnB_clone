#!/usr/bin/python3
'''testcase for amenity class'''
import unittest
import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''
    Test cases for the amenity class.
    '''
    def test_amenity(self):
        '''testing'''
        self.amenity = Amenity()
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)

        self.amenity.name = 'Ada'
        self.assertEqual(self.amenity.name, 'Ada')

        prev_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(prev_updated_at, self.amenity.updated_at)

        json_model = self.amenity.to_dict()
        self.assertIsInstance(json_model, dict)
        self.assertIn('__class__', json_model)
        self.assertEqual(json_model['__class__'], 'Amenity')
        self.assertIsInstance(json_model['id'], str)
        self.assertEqual(json_model['name'], 'Ada')
        self.assertIsInstance(json_model['created_at'], str)
        self.assertIsInstance(json_model['updated_at'], str)

    def test_amenity_with_kwargs(self):
        '''testing kwargs'''
        date = datetime.datetime.today()
        dt_frmt = date.isoformat()
        amenity = Amenity(
                id="345",
                name='George',
                created_at=dt_frmt,
                updated_at=dt_frmt
                )
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.name, "George")
        self.assertEqual(amenity.created_at, date)
        self.assertEqual(amenity.updated_at, date)

    def test_amenity_with_none_kwargs(self):
        '''testing'''
        with self.assertRaises(TypeError):
            Amenity(id=None, name='', created_at=None, updated_at=None)


        if __name__ == '__main__':
            unittest.main()
