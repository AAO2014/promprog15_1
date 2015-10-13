import unittest
from lesson4.classwork_2 import is_leap_year


class MyLeapYearTest(unittest.TestCase):

    def test_4(self):
        self.assertTrue(is_leap_year(4))

    def test_700(self):
        self.assertFalse(is_leap_year(700))
    def test_1400(self):
        self.assertFalse(is_leap_year(1400))
    def test_1800(self):
        self.assertFalse(is_leap_year(1800))
    def test_1600(self):
        self.assertTrue(is_leap_year(1600))
    def test_2000(self):
        self.assertTrue(is_leap_year(2000))



