#!/usr/bin/python3
'''testcase for state class'''
import unittest
import datetime
from models.state import State


class TestState(unittest.TestCase):
    '''
    Test cases for the State class.
    '''
    def test_state(self):
        '''testing'''
        self.state = State()
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime.datetime)
        self.assertIsInstance(self.state.updated_at, datetime.datetime)

        self.state.name = 'Ada'
        self.assertEqual(self.state.name, 'Ada')

        prev_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(prev_updated_at, self.state.updated_at)

        json_model = self.state.to_dict()
        self.assertIsInstance(json_model, dict)
        self.assertIn('__class__', json_model)
        self.assertEqual(json_model['__class__'], 'State')
        self.assertIsInstance(json_model['id'], str)
        self.assertEqual(json_model['name'], 'Ada')
        self.assertIsInstance(json_model['created_at'], str)
        self.assertIsInstance(json_model['updated_at'], str)

    def test_state_with_kwargs(self):
        '''testing'''
        date = datetime.datetime.today()
        dt_frmt = date.isoformat()
        state = State(
                id="345",
                name='George',
                created_at=dt_frmt,
                updated_at=dt_frmt
                )
        self.assertEqual(state.id, "345")
        self.assertEqual(state.name, "George")
        self.assertEqual(state.created_at, date)
        self.assertEqual(state.updated_at, date)

    def test_State_with_None_kwargs(self):
        '''testing'''
        with self.assertRaises(TypeError):
            State(id=None, name='', created_at=None, updated_at=None)


        if __name__ == '__main__':
            unittest.main()
