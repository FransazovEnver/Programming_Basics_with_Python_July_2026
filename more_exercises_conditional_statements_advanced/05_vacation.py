budget = float(input())
season = input()

location = ""
vacation = ""
price = 0.0

if budget <= 1000:
    vacation = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price -= (budget * 0.65)
    elif season == 'Winter':
        location = 'Morocco'
        price -= (budget * 0.45)
elif 1000 < budget <= 3000:
    vacation = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price -= (budget * 0.8)
    elif season == 'Winter':
        location = 'Morocco'
        price -= (budget * 0.6)
elif budget > 3000:
    vacation = 'Hotel'
    if season == 'Summer':
        location = 'Alaska'
        price -= (budget * 0.9)
    elif season == 'Winter':
        location = 'Morocco'
        price -= (budget * 0.9)

print(f'{location} - {vacation} - {abs(price):.2f}')
