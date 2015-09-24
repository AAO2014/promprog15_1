#!/usr/bin/env python
# -*- coding: utf-8 -*-

# напишите функцию, которая будет порождать исключение NotEqual,
# если её параметры не равны

class NotEqual(Exception):
    pass


def is_equal(param1, param2):
    if param1 <> param2:
        raise NotEqual(u"Параметры не равны!")  # для пайтона 2.7 нужно указывать юникодную строку


# обработайте это исключение при вызове функции
# напишите "числа равны" или "числа неравны"

a = 42
b = 42

try:
    is_equal(a, b)
except NotEqual:
    print u"Числа не равны"
else:
    print u"Числа равны."
