#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Заданы размеры А, В листа бумаги и x, y - размеры конверты
# Определить, поместится ли бумага в конверте


A, B = 8, 9
X, Y = 10, 7
X1, Y1 = 10, 17

def task1(a, b, x, y):
    if ((a <= x) and (b <= y)) or ((a <= y) and (b <= x)):
        return "yes"
    else:
       return "no"

print(task1(A, B, X, Y))
print(task1(A, B, X1, Y1))
# (**усложненное) Заданы размеры А, В прямоугольного отверстия и размеры х, у, z кирпича. 
# Определить, пройдет ли кирпич через отверстие.

hole = [3, 4]
brick = [10, 4, 2]
hole.sort()
brick.sort()

if (brick[0] <= hole[0] and brick[1] <= hole[1]):
    print("кирпич проходит в отверстие")
else:
    print("кирпич не проходит в отверстие")