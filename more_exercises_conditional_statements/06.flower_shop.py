from math import floor, ceil

MAGNOLIAS = 3.25
HYACINTHS = 4
ROSES = 3.50
CACTUS = 8

needed_flower = 0

magnolias_qty = int(input())
hyacinths_qty = int(input())
roses_qty = int(input())
cactus_qty = int(input())
gift = float(input())

sum_flowers = ((magnolias_qty * MAGNOLIAS) + (hyacinths_qty * HYACINTHS) +
               (roses_qty * ROSES) + (cactus_qty * CACTUS))

needed_flower = sum_flowers * 0.95

if needed_flower >= gift:
    print(f'She is left with {floor(needed_flower - gift)} leva.')
else:
    print(f'She will have to borrow {ceil(gift - needed_flower)} leva.')

