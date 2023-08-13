#!/usr/bin/python3
'''testcase for user class'''
import unittest
import datetime
from models.user import User


class TestUser(unittest.TestCase):
    '''
    Test cases for the User class.
    '''
    def test_user(self):
        '''testing'''
        self.user = User()
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime.datetime)
        self.assertIsInstance(self.user.updated_at, datetime.datetime)

        self.user.first_name = 'Ada'
        self.assertEqual(self.user.first_name, 'Ada')

        self.user.last_name = 'Okonkwo'
        self.assertEqual(self.user.last_name, 'Okonkwo')

        self.user.email = 'bene@gmail.com'
        self.assertEqual(self.user.email, 'bene@gmail.com')

        self.user.password = 'Adabe'
        self.assertEqual(self.user.password, 'Adabe')

        prev_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(prev_updated_at, self.user.updated_at)

        json_model = self.user.to_dict()
        self.assertIsInstance(json_model, dict)
        self.assertIn('__class__', json_model)
        self.assertEqual(json_model['__class__'], 'User')
        self.assertIsInstance(json_model['id'], str)
        self.assertEqual(json_model['first_name'], 'Ada')
        self.assertEqual(json_model['last_name'], 'Okonkwo')
        self.assertEqual(json_model['email'], 'bene@gmail.com')
        self.assertEqual(json_model['password'], 'Adabe')
        self.assertIsInstance(json_model['created_at'], str)
        self.assertIsInstance(json_model['updated_at'], str)

    def test_user_with_kwargs(self):
        '''testing'''
        date = datetime.datetime.today()
        dt_frmt = date.isoformat()
        user = User(
                id="345",
                password='adaa',
                email='ada@.com',
                first_name='George',
                last_name='Emetu',
                created_at=dt_frmt,
                updated_at=dt_frmt
                )
        self.assertEqual(user.id, "345")
        self.assertEqual(user.first_name, "George")
        self.assertEqual(user.last_name, "Emetu")
        self.assertEqual(user.email, "ada@.com")
        self.assertEqual(user.password, "adaa")
        self.assertEqual(user.created_at, date)
        self.assertEqual(user.updated_at, date)

    def test_user_with_none_kwargs(self):
        '''testing'''
        with self.assertRaises(TypeError):
            User(
                    id=None,
                    first_name="",
                    last_name="",
                    email='',
                    password='',
                    created_at=None,
                    updated_at=None
                    )


        if __name__ == '__main__':
            unittest.main()
