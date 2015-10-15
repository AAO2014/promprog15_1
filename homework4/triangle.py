#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Создать класс Треугольник. Треугольник задается тремя сторонами.
# Инициализатор должен выкидывать исключение BadTriangleException если заданы несовместные параметры
# Написать метод, который определяет площадь треугольника по формуле Герона
# Написать вспомогательный метод, который определяет полупериметр треугольника

from math import sqrt

a, b, c = 23, 120, 9


# Написать тесты на этот класс (в отдельном модуле)

class BadTreangleException(Exception):
    pass


class Triangle:
    def __init__(self, a, b, c):
        listOfSides = [a, b, c]
        listOfSides.sort()
        if listOfSides[0] <= 0 or ((listOfSides[0] + listOfSides[1]) <= listOfSides[2]):
            raise BadTreangleException("Bad lengths of the sides of a triangle")
            return
        self.a = a
        self.b = b
        self.c = c

    def half_perimeter(self):
        return (self.a + self.b + self.c) / 2

    def square(self):
        p = self.half_perimeter()
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


        # t = Triangle(a, b, c)
        # t = Triangle(2, 2, 2.828427125)
        # print t.square()
