allowed_bad_grades = int(input())

sum_grades = 0
numbers_solve_problems = 0
number_bad_grades = 0
last_task = 0

while allowed_bad_grades > number_bad_grades:
    command = input()

    if command == 'Enough':
        print(f'Average score: {sum_grades / numbers_solve_problems:.2f}')
        print(f'Number of problems: {numbers_solve_problems}')
        print(f'Last problem: {last_task}')
        break

    grade = int(input())

    if grade <= 4:
        number_bad_grades += 1

    sum_grades += grade
    numbers_solve_problems += 1
    last_task = command

else:
    print(f'You need a break, {number_bad_grades} poor grades.')