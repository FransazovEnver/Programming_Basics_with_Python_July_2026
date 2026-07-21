numbers_of_pages = int(input())
pages_for_one_hour = int(input())
numbers_of_days = int(input())

sum_hours = (numbers_of_pages / pages_for_one_hour) // numbers_of_days
print(sum_hours)
