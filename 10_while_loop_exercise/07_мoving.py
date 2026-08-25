width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())

box = width_free_space * length_free_space * height_free_space

number_free_space = 0

while box > number_free_space:
    command = input()

    if command == 'Done':
        print(f'{box - number_free_space} Cubic meters left.')
        break

    number_free_space += int(command)

else:
    print(f'No more free space! You need {number_free_space - box} Cubic meters more.')

