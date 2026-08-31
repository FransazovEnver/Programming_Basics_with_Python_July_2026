chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

price = 0
count = 0

if season == 'Spring' or 'Summer':
    chrysanthemums *= 2
    roses *= 4.10
    tulips *= 2.50
elif season == 'Autumn' or 'Winter':
    chrysanthemums *= 3.75
    roses *= 4.50
    tulips *= 4.15

price = chrysanthemums + roses + tulips

if season == 'Y':
    price += price * 0.15

if 7 < tulips:
    price -= price * 0.05

