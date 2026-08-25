coin = int(float(input()) * 100)

number = 0

while coin > 0:
    if coin >= 200:
        coin -= 200

    elif coin >= 100:
        coin -= 100

    elif coin >= 50:
        coin -= 50

    elif coin >= 20:
        coin -= 20

    elif coin >= 10:
        coin -= 10

    elif coin >= 5:
        coin -= 5

    elif coin >= 2:
        coin -= 2

    elif coin >= 1:
        coin -= 1

    number += 1

print(number)