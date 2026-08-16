fuel = input()
liters_fuel = int(input())

result = ""

if fuel == 'Diesel':
    if liters_fuel >= 25:
        result = f'You have enough diesel.'
    elif liters_fuel < 25:
        result = f'Fill your tank with diesel!'
    elif fuel != 'Diesel':
        result = 'Invalid fuel!'
elif fuel == 'Gasoline':
    if liters_fuel >= 25:
        result = f'You have enough gasoline.'
    elif liters_fuel < 25:
        result = f'Fill your tank with gasoline!'
    elif fuel != 'Gasoline':
        result = 'Invalid fuel!'
elif fuel == 'Gas':
    if liters_fuel >= 25:
        result = f'You have enough gas.'
    elif liters_fuel < 25:
        result = f'Fill your tank with gas!'
    elif fuel != 'Gas':
        result = 'Invalid fuel!'
else:
    result = 'Invalid fuel!'


print(result)
