#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Определить количество натуральных чисел из интервала от 100 до 500,
# сумма цифр которых равна 15

common_amount = 0
for number in range(100, 501):
    numeral_sum = 0
    for numeral in str(number):
        numeral_sum += int(numeral)
    if numeral_sum == 15:
        print('у числа', number, 'сумма цифр равна 15')
        common_amount += 1
print ('Количество натуральных чисел сумма цифр которых равна 15: ', common_amount)

# Определить количество трехзначных натуральных чисел,
# сумма цифр которых равна N (0 < N < 27)

amount = 0
for number in range(100,1000):
    numeral_sum = 0
    for numeral in str(number):
        numeral_sum += int(numeral)
    if 0 < numeral_sum < 27:
        print('у числа', number, 'сумма цифр > 0, но < 27')
        amount += 1
print ('Количество натуральных чисел сумма цифр которых > 0, но < 27: ', amount)
