
#Испытание 6.3. Найди самый короткий ряд закрашенных клеток.

from robot import *

c1 = 0 #up row
c2 = 0 #down row

while is_free_right():
    if(is_cell_painted()):
        c1 += 1
    move_right()

move_down()

while is_free_left():
    move_left()
    if(is_cell_painted()):
        c2 += 1

if (c1 < c2):
    move_up()
    for i in range(c1):
        move_right()
elif (c1 > c2):
    for i in range(c2):
        move_right()