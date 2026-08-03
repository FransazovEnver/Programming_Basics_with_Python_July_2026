BULGARIA_BUDGET = 100
BALKAN_BUDGET = 1000

budget = float(input())
season = input()

destination = ""
type_vacation = ""
spending_sum = 0

if season == 'summer':
    if budget <= BULGARIA_BUDGET:
        spending_sum = budget * 0.3
        type_vacation = 'Camp'
        destination = 'Bulgaria'
    elif BULGARIA_BUDGET < budget <= BALKAN_BUDGET:
        spending_sum = budget * 0.4
        type_vacation = 'Camp'
        destination = 'Balkans'
    else:
        spending_sum = budget * 0.9
        type_vacation = 'Hotel'
        destination = 'Europe'
elif season == 'winter':
    if budget <= BULGARIA_BUDGET:
        spending_sum = budget * 0.7
        type_vacation = 'Hotel'
        destination = 'Bulgaria'
    elif BULGARIA_BUDGET < budget <= BALKAN_BUDGET:
        spending_sum = budget * 0.8
        type_vacation = 'Hotel'
        destination = 'Balkans'
    else:
        spending_sum = budget * 0.9
        type_vacation = 'Hotel'
        destination = 'Europe'

print(f'Somewhere in {destination}')
print(f'{type_vacation} - {spending_sum:.2f}')
