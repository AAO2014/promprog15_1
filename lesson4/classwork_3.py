#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Дата некоторого дня определяется тремя натуральными числами y (год), m (месяц) и d (день).
# По заданным d, m и y определите дату предыдщуего дня.
#
# Заданный год может быть високосным. Год считается високосным, если его номер кратен 4,
# однако из кратных 100 високосными являются лишь кратные 400,
# например 1700, 1800 и 1900 — невисокосные года, 2000 — високосный.

from classwork_2 import is_leap_year
import math

class NonValidDataExeption

def yesterday(year, month, day):

    try
        if (0 <= int(year) <= 9999) and (0 < int(month) < 13) and (0 < int(day) < 32):
            if

    lenOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        lenOfMonths[1] = 29
    if (month == 1) and (day == 1):
        y = year - 1
        m = 12
        d = 31
    else:
        y = year
        if day == 1:
            m = month - 1
            d = lenOfMonths[m - 1]
        else:
            m = month
            d = day - 1

    return y, m, d

