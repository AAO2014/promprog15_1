#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# нарисовать снежинку с помощью функции snowflake
from random import randint
from simple_draw import snowflake, end, Point, clear_screen, user_want_exit, sleep

rays = [randint(30, 50) for i in range(5)]
velocities = [randint(10, 30) for i in range(5)]
y_coords = [500 for i in range(5)]

for step in range(20):
    clear_screen()
    for i in range(5):
        y_coords[i] -= velocities[i]
    for i in range(5):
        snowflake(center=Point(x=100 + i*100, y=y_coords[i]), length=rays[i])
    sleep(0.5)
    if user_want_exit():
        break

# параметризировать углы лучей снежинки, цвет рисования - передача разных параметров


end()


