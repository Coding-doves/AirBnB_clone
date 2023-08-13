#!/usr/bin/python3
'''testcase for place class'''
import unittest
import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    '''
    Test cases for the Place class.
    '''
    def test_place(self):
        '''testing'''
        self.place = Place()
        self.assertIsInstance(self.place.id, str)
        self.assertIsInstance(self.place.created_at, datetime.datetime)
        self.assertIsInstance(self.place.updated_at, datetime.datetime)

        self.place.name = 'Ada'
        self.place.city_id = '0987'
        self.place.user_id = '1298'
        self.place.description = 'Beautiful place'
        self.place.number_rooms = '204'
        self.place.number_bathrooms = '09'
        self.place.max_guest = '3'
        self.place.price_by_night = 'N2000'
        self.place.latitude = '0.7'
        self.place.longitude = '0.3'
        self.place.amenity_ids = '6759'

        self.assertEqual(self.place.name, 'Ada')
        self.assertEqual(self.place.city_id, '0987')
        self.assertEqual(self.place.user_id, '1298')
        self.assertEqual(self.place.description, 'Beautiful place')
        self.assertEqual(self.place.number_rooms, '204')
        self.assertEqual(self.place.number_bathrooms, '09')
        self.assertEqual(self.place.max_guest, '3')
        self.assertEqual(self.place.price_by_night, 'N2000')
        self.assertEqual(self.place.latitude, '0.7')
        self.assertEqual(self.place.longitude, '0.3')
        self.assertEqual(self.place.amenity_ids, '6759')

        prev_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(prev_updated_at, self.place.updated_at)

        json_model = self.place.to_dict()
        self.assertIsInstance(json_model, dict)
        self.assertIn('__class__', json_model)
        self.assertEqual(json_model['__class__'], 'Place')
        self.assertIsInstance(json_model['id'], str)
        self.assertEqual(json_model['name'], 'Ada')
        self.assertEqual(json_model['city_id'], '0987')
        self.assertEqual(json_model['user_id'], '1298')
        self.assertEqual(json_model['description'], 'Beautiful place')
        self.assertEqual(json_model['number_rooms'], '204')
        self.assertEqual(json_model['number_bathrooms'], '09')
        self.assertEqual(json_model['max_guest'], '3')
        self.assertEqual(json_model['price_by_night'], 'N2000')
        self.assertEqual(json_model['latitude'], '0.7')
        self.assertEqual(json_model['longitude'], '0.3')
        self.assertEqual(json_model['amenity_ids'], '6759')
        self.assertIsInstance(json_model['created_at'], str)
        self.assertIsInstance(json_model['updated_at'], str)

    def test_place_with_kwargs(self):
        '''testing'''
        date = datetime.datetime.today()
        dt_frmt = date.isoformat()
        place = Place(
                id="345",
                name='George',
                city_id='0023',
                user_id='0006',
                number_rooms='501',
                description='Hot view',
                number_bathrooms='1',
                max_guest='2',
                price_by_night='N1500',
                latitude='1.0',
                longitude='4.0',
                amenity_ids='0004',
                created_at=dt_frmt,
                updated_at=dt_frmt
                )
        self.assertEqual(place.id, "345")
        self.assertEqual(place.name, "George")
        self.assertEqual(place.city_id, "0023")
        self.assertEqual(place.user_id, "0006")
        self.assertEqual(place.description, "Hot view")
        self.assertEqual(place.number_rooms, "501")
        self.assertEqual(place.number_bathrooms, "1")
        self.assertEqual(place.max_guest, "2")
        self.assertEqual(place.price_by_night, "N1500")
        self.assertEqual(place.latitude, "1.0")
        self.assertEqual(place.longitude, "4.0")
        self.assertEqual(place.amenity_ids, "0004")
        self.assertEqual(place.created_at, date)
        self.assertEqual(place.updated_at, date)

    def test_place_with_none_kwargs(self):
        '''testing'''
        with self.assertRaises(TypeError):
            Place(
                    id=None,
                    name='',
                    city_id='',
                    user_id='',
                    description='',
                    number_rooms='',
                    number_bathrooms='',
                    max_guest='',
                    price_by_night='',
                    latitude='',
                    longitude='',
                    amenity_ids='',
                    created_at=None,
                    updated_at=None
                    )


        if __name__ == '__main__':
            unittest.main()
