type_product = input()
type_town = input()
quantity = float(input())

price = 0.0

if type_town == 'Sofia':
    if type_product == 'coffee':
        price = 0.50
    elif type_product == 'water':
        price = 0.80
    elif type_product == 'beer':
        price = 1.20
    elif type_product == 'sweets':
        price = 1.45
    elif type_product == 'peanuts':
        price = 1.60
elif type_town == 'Plovdiv':
    if type_product == 'coffee':
        price = 0.40
    elif type_product == 'water':
        price = 0.70
    elif type_product == 'beer':
        price = 1.15
    elif type_product == 'sweets':
        price = 1.30
    elif type_product == 'peanuts':
        price = 1.50
elif type_town == 'Varna':
    if type_product == 'coffee':
        price = 0.45
    elif type_product == 'water':
        price = 0.70
    elif type_product == 'beer':
        price = 1.10
    elif type_product == 'sweets':
        price = 1.35
    elif type_product == 'peanuts':
        price = 1.55

result = quantity * price

print(result)
