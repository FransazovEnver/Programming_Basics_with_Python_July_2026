budget = float(input())

product_count = 0.0
total_sum = 0.0

while True:
    command = input()

    if command == 'Stop':
        break

    price_product = float(input())
    product_count += 1

    if product_count % 3 == 0:
        total_sum += price_product / 2
    else:
        total_sum += price_product

if budget >= total_sum:
    print(f"You bought {product_count} products for {total_sum:.2f} leva.")
    print(f"Money left: {budget - total_sum:.2f} lv.")
else:
    print(f"Not enough money! You need {total_sum - budget:.2f} lv. more.")