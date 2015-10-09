#!/usr/bin/env python
# -*- coding: utf-8 -*-

# нарисовать снегопад - 7 движужихся снежинок радиусом от 10 до 60 
# снежинки падают с высоты 500 пикселов со скоростью 30 пикселов за такт
# на расстоянии 100 пикселов друг от друга
<<<<<<< HEAD
from simple_draw import clear_screen, Point, snowflake, sleep, end
from random import randint

### Радиусы случайные ###
# y = 500
# rad = [randint(10, 60) for i in range(7)]
# for i in range(10):
#     clear_screen()
#     y -= 30  # как изменяется y для всех снежинок
#     for i in range(7):
#         point = Point(i*100, y)
#         snowflake(point, length=rad[i])
#     sleep(0.01)
#


# # + нарисовать снежинки разных радиусов, для этого хранить список радиусов
radiuses = [30, 20, 40, 10, 50, 70, 60]
# y = 500
# for i in range(10):
#     clear_screen()
#     y -= 30  # как изменяется y для всех снежинок
#     for i in range(7):
#         point = Point(i*100, y)
#         snowflake(point, length=radiuses[i])
#     sleep(0.01)
# + сделать скорость падения уникальной для каждой снежинки,
# для этого хранить список координат Y и скоростей по Y

# ++ сделать реальный снегопад, что бы снежинки порхали из стороны в сторону
x_coords = [i*100 for i in range(7)]
#dx_coords = [randint(-5, 5) for i in range(7)]
coordinates = [500 for i in range(7)]
velocity = [randint(10, 50) for i in range(7)]
for i in range(15):
    clear_screen()
    for j in range(7):
        coordinates[j] -= velocity[j]  # как изменяется y для всех снежинок
        x_coords[j] += randint(-25,25)
    for z in range(7):
        point = Point(x_coords[z], coordinates[z])
        snowflake(point, length=radiuses[z])
    sleep(0.001)
=======
from simple_draw import clear_screen, Point, snowflake, sleep, end, COLOR_RED, user_want_exit


class SnowFlake:
    color = COLOR_RED

    def __init__(self, x=100, y=500):
        self._my_coord_x = x
        self._my_coord_y = y

    def move(self, dx=0, dy=0):
        self._my_coord_x += dx
        self._my_coord_y += dy

    def draw(self):
        point = Point(x=self._my_coord_x, y=self._my_coord_y)
        snowflake(center=point)

    @property
    def x(self):
        return self._my_coord_x

    @property
    def y(self):
        return self._my_coord_y


flakes = [SnowFlake(x=100 + i*100) for i in range(5)]

while True:
    clear_screen()
    for flake in flakes:
        if flake.y > 100:
            flake.move(dy=-50)
        flake.draw()
    sleep(0.5)
    if user_want_exit():
        break

>>>>>>> 0252ea3e8498c95e3b96d83f9a249324a8de3f22
end()


