first_number = int(input())
second_number = int(input())
operation = input()

result = ''

if operation == '+':
    result = (f'{first_number} + {second_number} = {first_number + second_number} '
              f'{"- even" if (first_number + second_number) % 2 == 0 else "- odd"}')

elif operation == '-':
    result = (f'{first_number} - {second_number} = {first_number - second_number} '
              f'{"- even" if (first_number - second_number) % 2 == 0 else "- odd"}')

elif operation == '*':
    result = (f'{first_number} * {second_number} = {first_number * second_number} '
              f'{"- even" if (first_number * second_number) % 2 == 0 else "- odd"}')

elif second_number == 0:
    result = f'Cannot divide {first_number} by zero'

elif operation == '/':
    result = f'{first_number} / {second_number} = {first_number / second_number:.2f}'

elif operation == '%':
    result = f'{first_number} % {second_number} = {first_number % second_number}'

print(result)