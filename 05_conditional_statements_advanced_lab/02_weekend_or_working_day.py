day_of_the_week = input()

result = ""

if day_of_the_week == 'Monday':
    result = 'Working day'
elif day_of_the_week == 'Tuesday':
    result = 'Working day'
elif day_of_the_week == 'Wednesday':
    result = 'Working day'
elif day_of_the_week == 'Thursday':
    result = 'Working day'
elif day_of_the_week == 'Friday':
    result = 'Working day'
elif day_of_the_week == 'Saturday':
    result = 'Weekend'
elif day_of_the_week == 'Sunday':
    result = 'Weekend'
else:
    result = 'Error'

print(result)