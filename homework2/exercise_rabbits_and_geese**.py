#!/usr/bin/env python
# -*- coding: utf-8 -*-

# У гусей и кроликов вместе 64 лапы. Сколько может быть кроликов и гусей (указать все сочетания)? 

total_legs = 64
total_vars = 0
for rabbits in range(0, 17):
    for geese in range(0, 33):
        if (rabbits * 4 + geese * 2) == total_legs:
            print ("rabbits = ", rabbits, " geese = ", geese)
        total_vars += 1
print ("total_vars = ", total_vars)


# оптимизировать количество переборов
total_legs = 64
total_vars = 0
for rabbits in range(0, 17):
    for geese in range(0, 33):
        if (rabbits * 4 + geese * 2) == total_legs:
            print ("rabbits = ", rabbits, " geese = ", geese)
            break;
        total_vars += 1
print ("total_vars = ", total_vars)


# оптимизировать количество переборов
total_legs = 64
total_vars = 0
for rabbits in range(0, 17):
    geese = int((total_legs - rabbits * 4)/2)
    print ("rabbits = ", rabbits, " geese = ", geese)
    total_vars += 1
print ("total_vars = ", total_vars)