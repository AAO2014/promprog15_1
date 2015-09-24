#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке
class ValueError(Exception):
    pass




zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# выдайте по запросу номер клетки, в которой сидит животное
# через функцию списка .index() : list.index(value)
# которая выбрасывает исключение IndexError если value нет в списке

#ask = 'elephant'
ask = 'bear'

# определите действия по подчистке - отпустите всех животных на волю

try:
    print zoo.index(ask)

except IndexError:
    # в задание закралась ошибка - здесь просто надо вывести на консоль сообщение
    print u"Такого животного нет!"

finally:
    zoo = []
    print "All animals are free!"
