PREMIERE = 12
NORMAL = 7.5
DISCOUNT = 5

screening_type = input()
rows = int(input())
columns = int(input())

result = 0

capacity = rows * columns

if screening_type == 'Premiere':
    result = capacity * PREMIERE
elif screening_type == 'Normal':
    result = capacity * NORMAL
elif screening_type == 'Discount':
    result = capacity * DISCOUNT

print(f'{result:.2f}')
