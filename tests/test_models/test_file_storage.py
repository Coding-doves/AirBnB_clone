#!/usr/bin/python3
'''testcase for filestorage class'''

import unittest
import os
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    '''
    Test cases for the filestorage class.

    '''
    def setUp(self):
        '''testing file_storage'''
        self.storage = FileStorage()

    def test_reload(self):
        '''testing'''
        # Create test instances for each class
        base_model = BaseModel()
        user = User()
        place = Place()
        state = State()
        city = City()
        amenity = Amenity()
        review = Review()

        # Adding instances using the new() => classes to __objects
        self.storage.new(base_model)
        self.storage.new(user)
        self.storage.new(place)
        self.storage.new(state)
        self.storage.new(city)
        self.storage.new(amenity)
        self.storage.new(review)

        # all() returns dictionary
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

        # Save to file and reload it
        self.storage.save()
        self.storage.reload()

        # Confirm if instances were reloaded correctly
        self.assertIn(
            f"{base_model.__class__.__name__}.{base_model.id}",
            self.storage.all()
        )

        self.assertIsNotNone(
            self.storage.all().get(f"{user.__class__.__name__}.{user.id}")
        )

        self.assertIsNotNone(
            self.storage.all().get(f"{place.__class__.__name__}.{place.id}")
        )

        self.assertIsNotNone(
            self.storage.all().get(f"{state.__class__.__name__}.{state.id}")
        )

        self.assertIsNotNone(
            self.storage.all().get(f"{city.__class__.__name__}.{city.id}")
        )

        self.assertIsNotNone(
            self.storage.all().get(
                f"{amenity.__class__.__name__}.{amenity.id}"
            )
        )

        self.assertIsNotNone(
            self.storage.all().get(f"{review.__class__.__name__}.{review.id}")
        )

    if __name__ == '__main__':
        unittest.main()
