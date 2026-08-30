locations = int(input())

for count in range(locations):
    average_gold = float(input())
    number_days = int(input())

    sum_gold = 0.0

    for day in range(number_days):
        gold_in_day = float(input())
        sum_gold += gold_in_day

    sum_average = sum_gold / number_days


    if sum_average >= average_gold:
        print(f'Good job! Average gold per day: {sum_average:.2f}.')
    else:
        print(f'You need {average_gold - sum_average:.2f} gold.')
