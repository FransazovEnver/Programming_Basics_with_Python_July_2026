budget = float(input())
needed_gas = float(input())
day_of_week = input()

liter_gas = 2.10
cicerone = 100

total_sum = (needed_gas * liter_gas) + cicerone

if day_of_week == 'Saturday':
    total_sum -= (total_sum * 0.1)
elif day_of_week == 'Sunday':
    total_sum -= (total_sum * 0.2)

if budget >= total_sum:
    print(f"Safari time! Money left: {budget - total_sum:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {total_sum - budget:.2f} lv.")
