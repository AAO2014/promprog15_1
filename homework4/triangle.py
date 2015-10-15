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
        # есть соглашение PEP8 http://astwild.blogspot.ru/2012/11/pep-8.html
        # давай использовать названия_с_подчеркиванием для переменных и имен методов
        # listOfSides -> list_of_sides -> просто sides
        # (в названиии переменной хранить её тип избыточно)
        sides = [a, b, c]
        sides.sort()
        if sides[0] <= 0 or ((sides[0] + sides[1]) <= sides[2]):
            raise BadTreangleException("Bad lengths of the sides of a triangle")
            return  # Этот ретурн никогда не сработает - в блоке кода все что после raise игнорируется
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
