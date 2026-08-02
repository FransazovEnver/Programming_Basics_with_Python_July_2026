SHIP_IN_SPRING = 3000
SHIP_IN_SUMMER_AND_AUTUMN = 4200
SHIP_IN_WINTER = 2600

budget = int(input())
season = input()
number_fishers = int(input())

price_for_rent = 0

if season == 'Spring':
    price_for_rent = SHIP_IN_SPRING

    if number_fishers <= 6:
        price_for_rent -= (price_for_rent * 0.1)
    elif 7 <= number_fishers <= 11:
        price_for_rent -= (price_for_rent * 0.15)
    elif number_fishers > 12:
        price_for_rent -= (price_for_rent * 0.25)
elif season == 'Summer' or season == 'Autumn':
    price_for_rent = SHIP_IN_SUMMER_AND_AUTUMN

    if number_fishers <= 6:
        price_for_rent -= (price_for_rent * 0.1)
    elif 7 <= number_fishers <= 11:
        price_for_rent -= (price_for_rent * 0.15)
    elif number_fishers > 12:
        price_for_rent -= (price_for_rent * 0.25)
elif season == 'Winter':
    price_for_rent = SHIP_IN_WINTER

    if number_fishers <= 6:
        price_for_rent -= (price_for_rent * 0.1)
    elif 7 <= number_fishers <= 11:
        price_for_rent -= (price_for_rent * 0.15)
    elif number_fishers > 12:
        price_for_rent -= (price_for_rent * 0.25)

if season != 'Autumn' and number_fishers % 2 == 0:
    price_for_rent -= (price_for_rent * 0.5)

if budget > price_for_rent:
    print(f'Yes! You have {budget - price_for_rent:.2f} leva left.')
else:
    print(f'Not enough money! You need {price_for_rent - budget:.2f} leva.')
