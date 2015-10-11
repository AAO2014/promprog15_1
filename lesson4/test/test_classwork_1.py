import unittest
from lesson4.classwork_1 import make_dict

__author__ = 'avis'


class MyDictTest(unittest.TestCase):

    def test_normal(self):
        res = make_dict(['a', 'b', 'c'], [1, 2])
        self.assertEqual(res, {'a':1, 'b':2, 'c':None})

    def test_morevalue(self):
        res = make_dict(['a', 'b', 'c'], [1, 2, 3, 4])
        self.assertEqual(res, {'a':1, 'b':2, 'c':3})

    def test_none(self):
        res = make_dict([], [])
        self.assertEqual(res, {})


