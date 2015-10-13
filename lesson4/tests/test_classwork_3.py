#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from classwork_3 import yesterday, NonValidDataExeption


class prevday(unittest.TestCase):

    def test_01_01(self):
        year, month, day = yesterday(2015, 1, 1)
        self.assertEqual(year, 2014)
        self.assertEqual(month, 12)
        self.assertEqual(day, 31)

    def test_12_31(self):
        year, month, day = yesterday(2015, 12, 31)
        self.assertEqual(year, 2015)
        self.assertEqual(month, 12)
        self.assertEqual(day, 30)

    def test_simple(self):
        year, month, day = yesterday(2015, 1, 15)
        self.assertEqual(year, 2015)
        self.assertEqual(month, 1)
        self.assertEqual(day, 14)

    def test_01_leap(self):
        year, month, day = yesterday(2000, 3, 1)
        self.assertEqual(year, 2000)
        self.assertEqual(month, 2)
        self.assertEqual(day, 29)

    def test_01_noleap(self):
        year, month, day = yesterday(2001, 3, 1)
        self.assertEqual(year, 2001)
        self.assertEqual(month, 2)
        self.assertEqual(day, 28)

    def test_exception(self):
        self.assertRaises(NonValidDataExeption, yesterday, year=2015, month=2, day=31)