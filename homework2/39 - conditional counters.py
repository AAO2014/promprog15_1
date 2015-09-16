#! /usr/bin/env python
# -*- coding: utf-8 -*-

my_list = [2, 3, 5, 7, 9, 13, 21, 25, 38, 42, 65, 90, ]

# разделить на 3.0 те элементы
# которые делятся нацело на 5
# в результате должен получится укороченный список my_list_3


# вариант 1 - c помощью цикла for
my_list_3 = []
for i in my_list:
    if i % 5 == 0:
        my_list_3 += [i/3.0]
print("Результат с помощью цикла:      ", my_list_3)


# вариант 2 - с помощью операций map и filter
def filter5(x):
    return x % 5 == 0

def third(x):
    return x/3.0

my_list_3 = list(map(third, filter(filter5, my_list)))
print("Результат с помощью map/filter: ", my_list_3)


# вариант 3 - с помощью спискового выражения с условием
my_list_3 = [x/3.0  for x in my_list if x%5 == 0]
print("Результат с помощью волшебства: ", my_list_3)