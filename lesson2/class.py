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
 
 

flakes = [SnowFlakes(x=100 + i*10) for i in range(5)]

while True:
    clear_screen()
    if sf1.y > 100:
        sf1.move(dy=-50)
    sf1.draw()
    sleep(0.5)
    if user_want_exit():
        break
 
end()