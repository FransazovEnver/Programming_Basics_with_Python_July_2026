FACEBOOK = 150
INSTAGRAM = 100
REDDIT = 50

numbers_of_tabs = int(input())
salary = int(input())

for _ in range(numbers_of_tabs):
    sites = input()

    if sites == 'Facebook':
        salary -= FACEBOOK

    elif sites == 'Instagram':
        salary -= INSTAGRAM

    elif sites == 'Reddit':
        salary -= REDDIT

    if salary <= 0:
        print('You have lost your salary.')
        break
else:
    print(f'{salary}')