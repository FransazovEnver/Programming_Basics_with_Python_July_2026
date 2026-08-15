number_of_kilometers= int(input())
day_or_night = input()

result = 0
taxi_start = 0.70
taxi_at_night = 0.90
taxi_at_day = 0.79
bus = 0.09
train = 0.06

if number_of_kilometers < 20:
    if day_or_night == 'day':
        result = taxi_start + (number_of_kilometers * taxi_at_day)
    elif day_or_night == 'night':
        result = taxi_start + (number_of_kilometers * taxi_at_night)
elif number_of_kilometers < 100:
    result = number_of_kilometers * bus
else:
    result = number_of_kilometers * train

print(f'{result:.2f}')
