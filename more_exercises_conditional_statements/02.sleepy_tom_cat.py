PLAYING_VACATION = 127
PLAYING_WHEN_WORK = 63
DAYS_IN_YEAR = 365
NORMAL_PLAYING_IN_YEAR = 30000

number_vacation_days = int(input())

working_days = DAYS_IN_YEAR - number_vacation_days

playing_time = (number_vacation_days * PLAYING_VACATION) + (working_days * PLAYING_WHEN_WORK)

sum_play = abs(NORMAL_PLAYING_IN_YEAR - playing_time)
hours = sum_play // 60
minutes = sum_play % 60

if playing_time > NORMAL_PLAYING_IN_YEAR:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')

elif NORMAL_PLAYING_IN_YEAR > playing_time:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')


