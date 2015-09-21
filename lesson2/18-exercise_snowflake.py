#!/usr/bin/env python
# -*- coding: utf-8 -*-

# нарисовать снежинку с помощью функции snowflake
from random import randint
from simple_draw import snowflake, end, Point, clear_screen,sleep


rays = [randint(30, 50) for i in range(5)]
speed = [randint(10, 30) for i in range(5)]
y_sf = [500 for i in range(5)]

for deltaY in range(0, 100, 10):
    clear_screen()
    for i in range(5):
        y_sf[i] -=  speed[i]
    for pos in range(5):
        snowflake(center=Point(x=100 + pos*100, y=y_sf[pos]), length=rays[pos])
    sleep(0.5)
# параметризировать углы лучей снежинки, цвет рисования - передача разных параметров

#snowflake(..., factor_a=0.2, ...)

end()


