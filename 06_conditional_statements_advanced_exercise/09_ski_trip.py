ROOM_FOR_ONE_PERSON = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35

days_of_stay = int(input()) - 1
room_type = input()
rating = input()

result = 0
rating_positive_negative = 0

if room_type == 'room for one person':
    result = days_of_stay * ROOM_FOR_ONE_PERSON

elif room_type == 'apartment':
    result = days_of_stay * APARTMENT
    if days_of_stay < 10:
        result -= (days_of_stay * APARTMENT) * 0.3
    elif 10 <= days_of_stay <= 15:
        result -= (days_of_stay * APARTMENT) * 0.35
    elif days_of_stay > 15:
        result -= (days_of_stay * APARTMENT) * 0.5

elif room_type == 'president apartment':
    result = days_of_stay * PRESIDENT_APARTMENT
    if days_of_stay < 10:
        result -= (days_of_stay * PRESIDENT_APARTMENT) * 0.1
    elif 10 <= days_of_stay <= 15:
        result -= (days_of_stay * PRESIDENT_APARTMENT) * 0.15
    elif days_of_stay > 15:
        result -= (days_of_stay * PRESIDENT_APARTMENT) * 0.2


if rating == 'positive':
    result += (result * 0.25)
elif rating == 'negative':
    result -= (result * 0.1)

print(f'{result:.2f}')