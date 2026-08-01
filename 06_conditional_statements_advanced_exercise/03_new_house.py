ROSES = 5
DAHLIAS = 3.8
TULIPS = 2.8
NARCISSUS = 3
GLADIOLUS = 2.5

type_flower = input()
number_of_flower = int(input())
budget = int(input())

sum_flower = 0

if type_flower == 'Roses':
    sum_flower = number_of_flower * ROSES

    if number_of_flower > 80:
        sum_flower -= (sum_flower * 0.1)

elif type_flower == 'Dahlias':
    sum_flower = number_of_flower * DAHLIAS

    if number_of_flower > 90:
        sum_flower -= (sum_flower * 0.15)

elif type_flower == 'Tulips':
    sum_flower = number_of_flower * TULIPS

    if number_of_flower > 80:
        sum_flower -= (sum_flower * 0.15)

elif type_flower == 'Narcissus':
    sum_flower = number_of_flower * NARCISSUS

    if number_of_flower < 120:
        sum_flower += (sum_flower * 0.15)

elif type_flower == 'Gladiolus':
    sum_flower = number_of_flower * GLADIOLUS

    if number_of_flower < 80:
        sum_flower += (sum_flower * 0.2)

if budget >= sum_flower:
    print(f"Hey, you have a great garden with {number_of_flower} "
              f"{type_flower} and {budget - sum_flower:.2f} leva left.")
else:
    print(f"Not enough money, you need {sum_flower - budget:.2f} leva more.")

