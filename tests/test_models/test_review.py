#!/usr/bin/python3
'''testcase for state class'''
import unittest
import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    '''
    Test cases for the Review class.
    '''
    def test_review(self):
        '''testing'''
        self.review = Review()
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime.datetime)
        self.assertIsInstance(self.review.updated_at, datetime.datetime)

        self.review.text = 'I loved ur packages'
        self.assertEqual(self.review.text, 'I loved ur packages')

        self.review.place_id = '50987'
        self.assertEqual(self.review.place_id, '50987')

        self.review.user_id = '3648'
        self.assertEqual(self.review.user_id, '3648')

        prev_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(prev_updated_at, self.review.updated_at)

        json_model = self.review.to_dict()
        self.assertIsInstance(json_model, dict)
        self.assertIn('__class__', json_model)
        self.assertEqual(json_model['__class__'], 'Review')
        self.assertIsInstance(json_model['place_id'], str)
        self.assertIsInstance(json_model['user_id'], str)
        self.assertEqual(json_model['text'], 'I loved ur packages')
        self.assertIsInstance(json_model['created_at'], str)
        self.assertIsInstance(json_model['updated_at'], str)

    def test_review_with_kwargs(self):
        '''testing'''
        date = datetime.datetime.today()
        dt_frmt = date.isoformat()
        review = Review(
                id="345",
                user_id='5678',
                place_id='4321',
                text='Good one',
                created_at=dt_frmt,
                updated_at=dt_frmt
                )
        self.assertEqual(review.id, "345")
        self.assertEqual(review.place_id, "4321")
        self.assertEqual(review.user_id, "5678")
        self.assertEqual(review.text, "Good one")
        self.assertEqual(review.created_at, date)
        self.assertEqual(review.updated_at, date)

    def test_review_with_none_kwargs(self):
        '''testing'''
        with self.assertRaises(TypeError):
            Review(
                    id=None,
                    text='',
                    user_id='',
                    place_id='',
                    created_at=None,
                    updated_at=None
                    )


        if __name__ == '__main__':
            unittest.main()
