yard_to_greening = float(input())

one_meter_to_greening = 7.61
yard_to_greening = yard_to_greening * one_meter_to_greening
discount = 0.18 * yard_to_greening
sum_of_products = yard_to_greening - discount

print(f'The final price is: {sum_of_products} lv.')
print(f'The discount is: {discount} lv."')