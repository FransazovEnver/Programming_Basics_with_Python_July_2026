from math import ceil

name_serial = input()
episode_time = int(input())
episode_break = int(input())

lunch_break = episode_break / 8
break_time = episode_break / 4
time_left = episode_break - (episode_time + lunch_break + break_time)

if time_left >= 0:
    print(f'You have enough time to watch {name_serial} and left with '
          f'{ceil(time_left)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_serial}, "
          f"you need {ceil(abs(time_left))} more minutes.")

