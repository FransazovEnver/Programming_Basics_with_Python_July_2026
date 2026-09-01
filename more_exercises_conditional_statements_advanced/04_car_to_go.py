budget = float(input())
season = input()

type_car = ""
type_class = ""
price = 0


if 100 >= budget:
    type_class = "Economy class"
    if season == 'Summer':
        type_car = 'Cabrio'
        price -= (budget * 0.35)
    elif season == 'Winter':
        type_car = 'Jeep'
        price -= (budget * 0.65)
elif 100 < budget <= 500:
    type_class = "Compact class"
    if season == 'Summer':
        type_car = 'Cabrio'
        price -= (budget * 0.45)
    elif season == 'Winter':
        type_car = 'Jeep'
        price -= (budget * 0.8)
elif 500 < budget:
    type_class = 'Luxury class'
    type_car = 'Jeep'
    price -= (budget * 0.9)



print(f'{type_class}')
print(f'{type_car} - {abs(price):.2f}')