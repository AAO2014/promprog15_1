#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from classwork_1 import make_dict, MakeListException


class MakeDictTest(unittest.TestCase):

    def test_equal(self):
        res = make_dict(keys_list=['a', 'b', 'c'], values_list=[1, 2, 3])
        self.assertEqual(res, dict(a=1, b=2, c=3))

    def test_exception(self):
        self.assertRaises(MakeListException, make_dict, keys_list=23, values_list=34)