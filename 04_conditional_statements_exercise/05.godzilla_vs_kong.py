budget_movie = float(input())
number_statists = int(input())
price_clothes = float(input())

decor_price = budget_movie * 0.1

clothes_price = number_statists * price_clothes

if number_statists > 150:
    clothes_price -= (clothes_price * 0.1)

sum_decor_and_clothes = clothes_price + decor_price

if sum_decor_and_clothes > budget_movie:
    print('Not enough money!')
    print(f'Wingard needs {sum_decor_and_clothes - budget_movie:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {budget_movie - sum_decor_and_clothes:.2f} leva left.')
