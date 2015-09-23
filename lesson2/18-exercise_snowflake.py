#!/usr/bin/env python
# -*- coding: utf-8 -*-

# нарисовать снежинку с помощью функции snowflake
from random import randint, random
from simple_draw import snowflake, end, Point, clear_screen


rays = [randint(30, 50) for i in range(5)]
speed = [randint(5, 50) for i in range(5)]
y_sf = [500 for i in range(5)]
f_a = [random() for i in range(5)]
f_b = [random() for i in range(5)]
f_c = [randint(15,90) for i in range(5)]
col = [[randint(0,255), randint(0,255), randint(0,255)] for i in range(5)]

for deltaY in range(0, 100, 10):
    clear_screen()
    for i in range(5):
        y_sf[i] -=  speed[i]
    for i in range(5):
        snowflake(center=Point(x=100 + i*100, y=y_sf[i]), length=rays[i], factor_a=f_a[i], factor_b=f_b[i], factor_c=f_c[i], color=col[i])

end()


