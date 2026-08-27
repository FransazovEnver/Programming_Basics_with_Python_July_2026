

judges = int(input())

total_sum_grades = 0
total_counts = 0
result = ""

while True:
    command = input()

    if command == 'Finish':
        break

    current_sum_grades = 0

    for _ in range(judges):
        grades = float(input())
        current_sum_grades += grades

    result += f'{command} - {current_sum_grades / judges:.2f}.\n'
    total_sum_grades += current_sum_grades
    total_counts += judges

result += f"Student's final assessment is {total_sum_grades / total_counts:.2f}."
print(result)