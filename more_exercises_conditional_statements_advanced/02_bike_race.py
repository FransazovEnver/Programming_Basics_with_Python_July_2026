junior_cyclists = int(input())
seniors_cyclists = int(input())
route = input()

sum_junior = 0
sum_senior = 0
total_sum = 0

if route == 'trail':
    sum_junior = junior_cyclists * 5.50
    sum_senior = seniors_cyclists * 7
elif route == 'cross-country':
    if junior_cyclists + seniors_cyclists >= 50:
        sum_junior = junior_cyclists * 8
        sum_junior -= sum_junior * 0.25
        sum_senior = seniors_cyclists * 9.50
        sum_senior -= sum_senior * 0.25
    else:
        sum_junior = junior_cyclists * 8
        sum_senior = seniors_cyclists * 9.50
elif route == 'downhill':
    sum_junior = junior_cyclists * 12.25
    sum_senior = seniors_cyclists * 13.75
elif route == 'road':
    sum_junior = junior_cyclists * 20
    sum_senior = seniors_cyclists * 21.50


total = sum_senior + sum_junior
total_sum = total - (total * 0.05)


print(f'{total_sum:.2f}')



