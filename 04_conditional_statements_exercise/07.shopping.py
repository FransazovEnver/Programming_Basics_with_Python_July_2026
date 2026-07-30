budget = float(input())
numbers_video_carts = int(input())
numbers_processors = int(input())
ram = int(input())

sum_video_carts = numbers_video_carts * 250
sum_materials = (sum_video_carts +
                 ((sum_video_carts * 0.35) * numbers_processors) +
                 ((sum_video_carts * 0.10) * ram))

if numbers_video_carts > numbers_processors:
    sum_materials -= (sum_materials * 0.15)

if budget >= sum_materials:
    print(f'You have {budget - sum_materials:.2f} leva left!')
else:
    print(f'Not enough money! You need {sum_materials - budget:.2f} leva more!')

