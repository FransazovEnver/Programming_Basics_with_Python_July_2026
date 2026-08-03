STUDIO_MAY_OCTOBER = 50
STUDIO_JUNE_SEPTEMBER = 75.20
STUDIO_JULY_AUGUST = 76

APARTMENT_MAY_OCTOBER = 65
APARTMENT_JUNE_SEPTEMBER = 68.70
APARTMENT_JULY_AUGUST = 77

studio = 0
apartment = 0

month = input()
number_of_night = int(input())

if month == "May" or month == 'October':
    apartment = number_of_night * APARTMENT_MAY_OCTOBER
    studio = number_of_night * STUDIO_MAY_OCTOBER

    if number_of_night > 14:
        studio -= (studio * 0.3)
    elif number_of_night > 7:
        studio -= (studio * 0.05)

elif month == 'June' or month == 'September':
    apartment = number_of_night * APARTMENT_JUNE_SEPTEMBER
    studio = number_of_night * STUDIO_JUNE_SEPTEMBER

    if number_of_night > 14:
        studio -= (studio * 0.2)

elif month == 'July' or month == 'August':
    apartment = number_of_night * APARTMENT_JULY_AUGUST
    studio = number_of_night * STUDIO_JULY_AUGUST

if number_of_night > 14:
    apartment -= (apartment * 0.1)

print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')


