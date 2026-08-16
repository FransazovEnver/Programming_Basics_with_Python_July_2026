from math import ceil, floor

number_days = int(input())
food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input()) / 1000

result = 0

needed_food = ((number_days * dog_food) + (number_days * cat_food) +
               (number_days * turtle_food))

if needed_food <= food:
    print(f'{floor(food - needed_food)} kilos of food left.')
else:
    print(f'{ceil(needed_food - food)} more kilos of food are needed.')

