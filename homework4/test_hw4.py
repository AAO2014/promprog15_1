import unittest
from triangle import Triangle, BadTreangleException

class TriangleTest(unittest.TestCase):

    def test_exception_toolongside(self):
        self.assertRaises(BadTreangleException, Triangle, 1, 2, 5)

    def test_exception_onezero1(self):
        self.assertRaises(BadTreangleException, Triangle, 0, 2, 3)

    def test_exception_onezero3(self):
        self.assertRaises(BadTreangleException, Triangle, 1, 2, 0)

    def test_exception_negativeside(self):
        self.assertRaises(BadTreangleException, Triangle, -1, 2, 3)

    def test_exception_allzero(self):
        self.assertRaises(BadTreangleException, Triangle, 0, 0, 0)

    def test_square_2(self):
        t = Triangle(2, 2, 2.828427125)
        self.assertEqual(t.square(), 2)