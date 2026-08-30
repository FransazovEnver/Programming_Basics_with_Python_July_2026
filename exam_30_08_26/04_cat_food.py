PRICE_FOOD = 12.45

number_cats = int(input())

group1 = 0
group2 = 0
group3 = 0
total_food_grams = 0

for i in range(number_cats):
    cat_food = float(input())
    total_food_grams += cat_food

    if 100 <= cat_food < 200:
        group1 += 1
    elif 200 <= cat_food < 300:
        group2 += 1
    elif 300 <= cat_food < 400:
        group3 += 1

total_kg = total_food_grams / 1000
total_cost = total_kg * PRICE_FOOD

print(f"Group 1: {group1} cats.")
print(f"Group 2: {group2} cats.")
print(f"Group 3: {group3} cats.")
print(f"Price for food per day: {total_cost:.2f} lv.")