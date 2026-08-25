GOAL = 10000

sum_steps = 0

while sum_steps < GOAL:
    command = input()

    if command == 'Going home':
        steps_to_home = int(input())
        sum_steps += steps_to_home
        break

    sum_steps += int(command)

if sum_steps >= GOAL:
    print('Goal reached! Good job!')
    print(f'{sum_steps - GOAL} steps over the goal!')
else:
    print(f'{GOAL - sum_steps} more steps to reach goal.')