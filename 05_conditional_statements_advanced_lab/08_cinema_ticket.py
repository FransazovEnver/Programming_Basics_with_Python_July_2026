day_of_week = input()

tickets = ""

if day_of_week == 'Monday':
    tickets = 12
elif day_of_week == 'Tuesday':
    tickets = 12
elif day_of_week == 'Wednesday':
    tickets = 14
elif day_of_week == 'Thursday':
    tickets = 14
elif day_of_week == 'Friday':
    tickets = 12
elif ((day_of_week == 'Saturday')
    or (day_of_week == 'Sunday')):
    tickets = 16

print(tickets)
