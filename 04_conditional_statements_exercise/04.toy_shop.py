PUZZEL = 2.60
TALKIN_DOLL = 3
TOY_BEAR = 4.1
MINION = 8.2
TOY_TRUCK = 2

price_vacantion = float(input())
number_puzzel = int(input())
number_doll = int(input())
number_bear = int(input())
number_minion = int(input())
number_truck = int(input())

sum_toys = number_puzzel + number_doll + number_bear + number_minion + number_truck
all_toys_price = ((number_puzzel * PUZZEL) + (number_doll * TALKIN_DOLL) +
                  (number_bear * TOY_BEAR) + (number_minion * MINION) +
                  (number_truck * TOY_TRUCK))

if sum_toys >= 50:
    all_toys_price -= (all_toys_price * 0.25)

all_toys_price -= (all_toys_price * 0.1)

if all_toys_price >= price_vacantion:
    print(f'Yes! {all_toys_price - price_vacantion:.2f} lv left.')
else:
    print(f'Not enough money! {price_vacantion - all_toys_price:.2f} lv needed.')
