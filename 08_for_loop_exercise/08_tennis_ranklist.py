WIN = 2000
FINAL = 1200
SEMIFINAL = 720

number_of_tournament = int(input())
number_points = int(input())

final_point = 0
number_win = 0

for _ in range(number_of_tournament):
    level_in_tournament = input()

    if level_in_tournament == 'W':
        number_win += 1
        final_point += WIN

    elif level_in_tournament == 'F':
        final_point += FINAL

    elif level_in_tournament == 'SF':
        final_point += SEMIFINAL

print(f'Final points: {final_point + number_points}')
print(f'Average points: {final_point // number_of_tournament}')
print(f'{number_win / number_of_tournament * 100:.2f}%')