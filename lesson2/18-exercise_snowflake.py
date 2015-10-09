#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# нарисовать снежинку с помощью функции snowflake
<<<<<<< HEAD
from random import randint, random
from simple_draw import snowflake, end, Point, clear_screen

=======
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
>>>>>>> 0252ea3e8498c95e3b96d83f9a249324a8de3f22

rays = [randint(30, 50) for i in range(5)]
speed = [randint(5, 50) for i in range(5)]
y_sf = [500 for i in range(5)]
f_a = [random() for i in range(5)]
f_b = [random() for i in range(5)]
f_c = [randint(15,90) for i in range(5)]
col = [[randint(0,255), randint(0,255), randint(0,255)] for i in range(5)]

<<<<<<< HEAD
for deltaY in range(0, 100, 10):
    clear_screen()
    for i in range(5):
        y_sf[i] -=  speed[i]
    for i in range(5):
        snowflake(center=Point(x=100 + i*100, y=y_sf[i]), length=rays[i], factor_a=f_a[i], factor_b=f_b[i], factor_c=f_c[i], color=col[i])
=======
>>>>>>> 0252ea3e8498c95e3b96d83f9a249324a8de3f22

end()


