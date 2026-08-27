number = int(input())

for num in range(1111, 10000):
    for digit in str(num):

        if digit == '0':
            break

        if number % int(digit):
            break
    else:
        print(num, end=' ')