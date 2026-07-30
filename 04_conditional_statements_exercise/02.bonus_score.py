staring_point = int(input())

bonus_point = 0

if staring_point < 100:
    bonus_point = 5
elif 100 < staring_point <= 1000:
    bonus_point = staring_point * 0.20
elif staring_point > 1000:
    bonus_point = staring_point * 0.10

if staring_point % 2 == 0:
    bonus_point += 1
elif staring_point % 10 == 5:
    bonus_point += 2

print(bonus_point)
print(staring_point + bonus_point)