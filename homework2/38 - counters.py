#! /usr/bin/env python
# -*- coding: utf-8 -*-

my_list = [2, 3, 5, 7, 9, 13, 21, 27, 42, 99, ]

# разделить каждый элемент списка на 3.0
# в результате должен получится список my_list_2


my_list_2 = []
# вариант 1 - c помощью цикла for 
for i in my_list:
    my_list_2 += [i/3]
print("Делим элементы списка на 3 с помощью for: ", my_list_2)


# вариант 2 - с помощью операции map
def third(x):
    return x/3.0

my_list_2 = list(map(third, my_list))
print("Делим элементы списка на 3 с помощью map: ", my_list_2)


# вариант 3 - с помощью спискового выражения
my_list_2 = [x/3.0 for x in my_list]
print("Делим элементы списка на 3 с помощью чар: ", my_list_2)
