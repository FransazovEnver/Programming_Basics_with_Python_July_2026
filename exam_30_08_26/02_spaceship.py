from math import floor

ROOM_WIDTH = 2
ROOM_LENGTH = 2
AVERAGE_ASTRONAUTS = 0.40

width = float(input())
length = float(input())
height = float(input())
average_height_astronauts = float(input())

spacecraft = width * length * height
room_space = ((average_height_astronauts + AVERAGE_ASTRONAUTS) *
              ROOM_WIDTH * ROOM_LENGTH)
number_astronauts = floor(spacecraft / room_space)

if 3 < number_astronauts <= 10:
    print(f'The spacecraft holds {number_astronauts} astronauts.')
elif number_astronauts < 3:
    print(f'The spacecraft is too small.')
elif number_astronauts > 10:
    print('The spacecraft is too big.')
