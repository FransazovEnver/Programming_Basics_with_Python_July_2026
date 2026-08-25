width_cake = int(input())
length_cake = int(input())

size = width_cake * length_cake

pieces = 0

while pieces < size:
    command = input()

    if command == 'STOP':
        print(f'{size - pieces} pieces are left.')
        break

    pieces += int(command)

else:
    print(f'No more cake left! You need {pieces - size} pieces more.')

