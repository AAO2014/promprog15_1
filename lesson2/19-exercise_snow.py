#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from simple_draw import snowflake, end, Point
# нарисовать снег - 1000 снежинок радиусом от 10 до 60 в произвольных местах экрана,
from simple_draw import snowflake, end


for i in range(0,1000):
    position = [randint(0, 500), randint(0, 500)]
    ray = randint(10, 60)
    snowflake(center=Point(position[0],position[1]), length=ray)

end()


