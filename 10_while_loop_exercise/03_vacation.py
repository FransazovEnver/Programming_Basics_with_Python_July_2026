needed_money = float(input())
balance = float(input())

number_days = 0
count_spending_days = 0

while count_spending_days < 5:
    action = input()
    money = float(input())

    number_days += 1

    if action == 'spend':
        count_spending_days += 1
        balance = balance - money if balance > money else 0

    elif action == 'save':
        count_spending_days = 0
        balance += money

        if balance >= needed_money:
            print(f'You saved the money for {number_days} days.')
            break
else:
    print(f"You can't save the money.")
    print(number_days)