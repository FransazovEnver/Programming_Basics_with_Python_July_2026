season = input()
distance = float(input())

price = 0.0
total_salary= 0.0

if 5000 >= distance:
    if season == "Spring" or season == "Autumn":
        price = 0.75
    elif season == "Summer":
        price = 0.90
    elif season == "Winter":
        price = 1.05
elif 5000 < distance <= 10000:
    if season == "Spring" or season == "Autumn":
        price = 0.95
    elif season == "Summer":
        price = 1.1
    elif season == "Winter":
        price = 1.25
elif 10000 < distance <= 20000:
    price = 1.45

#not working properly needed refact
salary = (distance * price) * 4
total_salary -= (salary * 0.1)

print(f'{total_salary:.2f}')