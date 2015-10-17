#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function  # для совместимости с python 2.x.x

# Дата некоторого дня определяется тремя натуральными числами y (год), m (месяц) и d (день).
# По заданным d, m и y определите дату предыдщуего дня.
#
# Заданный год может быть високосным. Год считается високосным, если его номер кратен 4,
# однако из кратных 100 високосными являются лишь кратные 400,
# например 1700, 1800 и 1900 — невисокосные года, 2000 — високосный.

from classwork_2 import is_leap_year

# lenOfMonths -> months_lengths
months_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class NonValidDataExeption(Exception):
    pass


def yesterday(year, month, day):
    try:
        if not ((0 <= int(year) <= 9999) and (0 < int(month) < 13) and (0 < int(day) < 32)):
            print("Data isn't correct")  # мы договорились что пишем на 3м пайтоне => print()
            # здесь по логике тоже надо скидывать NonValidDataExeption
            return None
    except:
        raise NonValidDataExeption("Data isn't integer number")
        # здесь по логике тоже надо скидывать NonValidDataExeption
        return None

    if day > months_lengths[month - 1]:
        # в сообщении Exception нужно максимально детализировать ошибку
        # - что было передано, какие значения допустимы
        # NonValidDataExeption("Month {} isn't correct! Valid values is {}-{}".format(...))
        raise NonValidDataExeption("Month isn't correct")

    if is_leap_year(year):
        months_lengths[1] = 29
    else:
        months_lengths[1] = 28

    if (month == 1) and (day == 1):
        y = year - 1
        m = 12
        d = 31
    else:
        y = year
        if day == 1:
            m = month - 1
            d = months_lengths[m - 1]
        else:
            m = month
            d = day - 1

    return y, m, d
