#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from classwork_2 import is_leap


class IsLeapTest(unittest.TestCase):

    def test_16(self):
        self.assertTrue(is_leap(16))

    def test_15(self):
        self.assertFalse(is_leap(15))

    def test_700(self):
        self.assertFalse(is_leap(700))

    def test_1400(self):
        self.assertFalse(is_leap(1400))

    def test_1800(self):
        self.assertFalse(is_leap(1800))

    def test_1600(self):
        self.assertTrue(is_leap(1600))
