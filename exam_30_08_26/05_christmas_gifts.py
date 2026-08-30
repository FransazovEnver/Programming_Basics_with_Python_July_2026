TOY = 5
SWEATER = 15

kids = 0
adults = 0

while True:
    command = input()

    if command == 'Christmas':
        break

    age = int(command)

    if age <= 16:
        kids += 1
    else:
        adults += 1

toy_money = kids * TOY
sweater_money = adults * SWEATER

print(f'Number of adults: {adults}')
print(f'Number of kids: {kids}')
print(f'Money for toys: {toy_money}')
print(f'Money for sweaters: {sweater_money}')



