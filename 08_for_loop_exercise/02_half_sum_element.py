import sys

number_element = int(input())

max_element = -sys.maxsize
sum_element = 0

for _ in range(number_element):
    num = int(input())

    if num > max_element:
        max_element = num

    sum_element += num

half_sum = sum_element - max_element

if max_element == half_sum:
    print(f'Yes')
    print(f'Sum = {max_element}')
else:
    #sum_element = sum_element - max_element
    print('No')
    print(f'Diff = {abs(max_element - half_sum)}')