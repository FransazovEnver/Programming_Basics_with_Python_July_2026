CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETARIAN_MENU = 8.15
DELIVERY = 2.5

count_chicken_menu = int(input())
count_fish_menu = int(input())
count_veg_menu = int(input())

total_order = ((count_chicken_menu * CHICKEN_MENU) + (count_fish_menu * FISH_MENU)
               + (count_veg_menu * VEGETARIAN_MENU))
dessert = total_order * 0.20
total_sum = total_order + dessert + DELIVERY

print(total_sum)

