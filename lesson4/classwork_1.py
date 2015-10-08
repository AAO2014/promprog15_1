#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть два списка разной длины. В первом содержатся ключи, а во втором значения.
# Напишите функцию, которая создаёт из этих ключей и значений словарь.
# Если ключу не хватило значения, в словаре должно быть значение None.
# Значения, которым не хватило ключей, нужно игнорировать.
import unittest


class MakeListException(Exception):
    pass


def make_dict(keys_list, values_list):
    if not isinstance(keys_list, list) or not isinstance(values_list, list):
        raise MakeListException('make_dict() takes lists on its params!')
    res_dict = {}
    for i, key in enumerate(keys_list):
        res_dict[key] = values_list[i]
    return res_dict


if __name__ == '__main__':
    unittest.main()
