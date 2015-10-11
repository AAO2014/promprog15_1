#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from classwork_3 import yesterday


class IsLeapTest(unittest.TestCase):

    def test_01_01(self):
        year, month, day = yesterday(2015, 1, 1)
        self.assertEqual(year, 2014)
        self.assertEqual(month, 12)
        self.assertEqual(day, 31)

    def test_simple(self):
        year, month, day = yesterday(2015, 1, 15)
        self.assertEqual(year, 2015)
        self.assertEqual(month, 1)
        self.assertEqual(day, 14)
