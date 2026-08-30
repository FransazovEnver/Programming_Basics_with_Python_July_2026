from math import ceil, floor

budget = float(input())
ticket = input()
group = int(input())

sum_ticket = 0.0
result = ""

if 1 <= group <= 4:
    budget -= (budget * 0.75)
elif 5 <= group <= 9:
    budget -= (budget * 0.60)
elif 10 <= group <= 24:
    budget -= (budget * 0.50)
elif 25 <= group <= 49:
    budget -= (budget * 0.40)
elif 50 <= group:
    budget -= (budget * 0.25)

if ticket == 'Normal':
    sum_ticket += 249.99
elif ticket == 'VIP':
    sum_ticket += 499.99

total = sum_ticket * group

if budget >= total:
    result = f'Yes! You have {budget - total:.2f} leva left.'
elif budget <= total:
    result = f'Not enough money! You need {total - budget:.2f} leva.'

print(result)

