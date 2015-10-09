#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть два списка разной длины. В первом содержатся ключи, а во втором значения.
# Напишите функцию, которая создаёт из этих ключей и значений словарь.
# Если ключу не хватило значения, в словаре должно быть значение None.
# Значения, которым не хватило ключей, нужно игнорировать.

import unittest


def make_dict(keys, values):
    dictionary = {}
    for i in range(len(keys)):
        if len(values)-1 < i:
            dictionary[keys[i]] = None
        else:
            dictionary[keys[i]] = values[i]
    return dictionary


