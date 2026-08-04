exam_hour = int(input())
exam_minutes = int(input())
arrived_hour = int(input())
arrived_minutes = int(input())

exam_minutes = (exam_hour * 60) + exam_minutes
arrived_minutes = (arrived_hour * 60) + arrived_minutes

time_diff = exam_minutes - arrived_minutes

if time_diff > 30:
    print('Early')
elif time_diff < 0:
    print('Late')
else:
    print('On Time')

hour = abs(time_diff) // 60
minutes = abs(time_diff) % 60

result = ''

if hour > 0:
    result += f"{hour}:{minutes:02d} hours"
elif minutes > 0:
    result += f"{minutes} minutes"

if time_diff > 0:
    result += " before the start"
elif time_diff < 0:
    result += " after the start"

print(result)
