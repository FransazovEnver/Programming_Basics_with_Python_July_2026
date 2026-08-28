contract_term = input()
type_contract = input()
mobile_internet = input()
payment_month = int(input())

fee = 0.0

if contract_term == 'one':
    if type_contract == 'Small':
        fee = 9.98
    elif type_contract == 'Middle':
        fee = 18.99
    elif type_contract == 'Large':
        fee = 25.98
    elif type_contract == 'ExtraLarge':
        fee = 35.99
elif contract_term == 'two':
    if type_contract == 'Small':
        fee = 8.58
    elif type_contract == 'Middle':
        fee = 17.09
    elif type_contract == 'Large':
        fee = 23.59
    elif type_contract == 'ExtraLarge':
        fee = 31.79


if mobile_internet == 'yes':
    if fee <= 10.00:
        fee += 5.50
    elif fee <= 30.00:
        fee += 4.35
    elif fee > 30:
        fee += 3.85

if contract_term == "two":
    fee -= fee * (3.75 / 100)

total_fee = fee * payment_month

print(f'{total_fee:.2f} lv.')
