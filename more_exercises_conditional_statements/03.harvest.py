from math import  floor, ceil

vineyard = int(input())
grapes = float(input())
needed_wine = int(input())
workers = int(input())

needed_grapes_for_wine = 2.5

sum_grapes = (vineyard * grapes)
wine = (sum_grapes * 0.4) / needed_grapes_for_wine

if wine >= needed_wine:
    print(f'Good harvest this year! Total wine: {floor(wine)} liters.')
    print(f'{ceil(wine - needed_wine)} liters left -> {ceil((wine - needed_wine) / workers)} liters per person.')
elif wine <= needed_wine:
    print(f'It will be a tough winter! More {floor(needed_wine - wine)} liters wine needed.')