#!/usr/bin/env python
# -*- coding: utf-8 -*-

# умножение на пятый элемент
#
# возвести константу BRUCE_WILLIS в степень
# заданную цифрой в пятой позиции входной строки
#
# обработать исключительные ситуации 
# ValueError - невозможно преобразовать к числу
# IndexError - выход за границы списка

BRUCE_WILLIS = 42.0

good = False
while not good:
    try:
        input_data = raw_input('Enter elements:')
        lilu = int(input_data[4])
        good = True
        print "Получилось: ", BRUCE_WILLIS ** lilu

    except ValueError:
        print ("Невозможно преобразовать к числу. Вводите корректные данные!")

    except IndexError:
        print("Введнная строк слишком коротка!")








