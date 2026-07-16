GREEN_PAINT_COST = 3.4
RED_PAINT_COST = 4.3
WINDOW_AREA = 1.5
DOOR_WIGHT = 1.2
DOOR_HEIGHT = 2

number_x = float(input())
number_y = float(input())
number_h = float(input())

side_wall = number_x * number_y
window = WINDOW_AREA * WINDOW_AREA
sum_wall = (2 * side_wall) - (2 * window)
back_wall = number_x * number_x
door = DOOR_WIGHT * DOOR_HEIGHT
sum_front_back_walls =  2 * back_wall - door
sum_house = sum_wall + sum_front_back_walls
green_paint = sum_house / GREEN_PAINT_COST

two_side_of_roof = 2 * (number_x * number_y)
two_triangles = 2 * ((number_x * number_h) / 2)
sum_roof = two_side_of_roof + two_triangles
red_paint = sum_roof / RED_PAINT_COST


print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')