lili_age = int(input())
washing_machine = float(input())
price_of_toys = int(input())

BEGINNING_MONEY = 10
BROTHER_MONEY = 1

sum_money = 0
total_toys = 0

for lili_age in range(1, lili_age + 1):
    if lili_age % 2 == 0:
        sum_money += (BEGINNING_MONEY - BROTHER_MONEY)
        BEGINNING_MONEY += 10
    else:
        total_toys += 1

sum_money += (total_toys * price_of_toys)

if sum_money >= washing_machine:
    print(f'Yes! {sum_money - washing_machine:.2f}')
else:
    print(f'No! {washing_machine - sum_money:.2f}')