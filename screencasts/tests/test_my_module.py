#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from my_module import my_sort


class MyListTest(unittest.TestCase):

    def _my_func(self):
        print("ой-ой!")

    def test_normal(self):
        res = my_sort([4, 3, 5, 7, 1, 3, 2])
        self.assertEqual(res, [1, 2, 3, 4, 5, 7])

    def test_empty(self):
        res = my_sort([])
        self.assertEqual(res, [])

    def test_single(self):
        res = my_sort([6])
        self.assertEqual(res, [6])

    def test_negative(self):
        res = my_sort([3, 4, -5, 6, -7])
        self.assertEqual(res, [-7, -5, 3, 4, 6])

    def test_abc(self):
        res = my_sort(['d', 'c', 'a', 'b'])
        self.assertEqual(res, ['a', 'b', 'c', 'd'])