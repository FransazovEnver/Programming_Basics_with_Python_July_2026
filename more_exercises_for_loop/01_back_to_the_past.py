money = float(input())
year = int(input())

spent_money = 0
current_year = 18

for num in range(1800, year + 1):
    if num % 2 == 0:
        spent_money += 12000
    else:
        spent_money += 12000 + (50 * current_year)

    current_year += 1

if money >= spent_money:
    total = money - spent_money
    print(f"Yes! He will live a carefree life and will have {total:.2f} dollars left." )
else:
    needed = spent_money - money
    print(f"He will need {needed:.2f} dollars to survive." )