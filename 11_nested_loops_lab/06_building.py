sum_floors = int(input())
sum_rooms = int(input())

for floor in range(sum_floors, 0, -1):
    for room in range(sum_rooms):
        if floor == sum_floors:
            print(f'L{floor}{room}', end=' ')
        elif floor % 2 == 0:
            print(f'O{floor}{room}', end=' ')
        elif floor % 2 != 0:
            print(f'A{floor}{room}', end=' ')

    print()


