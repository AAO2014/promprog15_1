#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce

words = [u'Я', u'помню', u'чудное', u'мгновение', 
u'передо', u'мной', u'явилась', u'ты', ]

# выдать список длинн слов с помощью операции map
words_lengths = list(map(len, words))
print("Список длин слов: ", words_lengths)
# отфильтровать только длины слов, которые больше 4

def len_gt_4(param):
    return param > 4
words_lengths = list(filter(len_gt_4, words_lengths))
print("Список длин слов в которых больше 4х букв: ", words_lengths)

# выдать сумму длин слов, длинна которых > 4

def summ(x, y):
    return x + y

print ("Cумма длин слов у которых больше 4х букв: ", reduce(summ, words_lengths))
