#!/usr/bin/env python
# -*- coding: utf-8 -*-

# вывести на консоль жителей комнаты 1 и 2 (модули room1 и room2)
# функция get_inhabitants возвращает список имен жителей
# Комната 1: Вася, Петя, Коля

import room1, room2


print ("В комнате 1 живут: ", ", ".join(room1.get_inhabitants()))
print ("В комнате 2 живут: ", ", ".join(room2.get_inhabitants()))
