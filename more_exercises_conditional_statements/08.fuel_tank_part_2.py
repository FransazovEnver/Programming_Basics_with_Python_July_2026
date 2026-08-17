fuel = input()
qty_fuel = float(input())
club_cart = input()

price = 0
total_price = 0

GASOLINE = 2.22
DIESEL = 2.33
GAS = 0.93

CLUB_CART_GASOLINE = 0.18
CLUB_CART_GAS = 0.08
CLUB_CART_DIESEL = 0.12

if fuel == 'Gasoline':
    price = GASOLINE
    if club_cart == 'Yes':
       price -= CLUB_CART_GASOLINE
elif fuel == 'Gas':
    price = GAS
    if club_cart == 'Yes':
       price -= CLUB_CART_GAS
elif fuel == 'Diesel':
    price = DIESEL
    if club_cart == 'Yes':
        price -= CLUB_CART_DIESEL

total_price = qty_fuel * price

if 20 <= qty_fuel <= 25:
    total_price -= total_price * 0.08
elif qty_fuel > 25:
    total_price -= total_price * 0.1


print(f'{total_price:.2f} lv.')
