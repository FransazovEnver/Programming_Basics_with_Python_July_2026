strawberry_price = float(input())
qty_banana = float(input())
qty_orange = float(input())
qty_raspberries = float(input())
qty_strawberry = float(input())

price_raspberries = strawberry_price - (strawberry_price * 0.5)
price_orange = price_raspberries - (price_raspberries * 0.4)
price_banana = price_raspberries - (price_raspberries * 0.8)

total_sum = ((price_raspberries * qty_raspberries) + (price_orange * qty_orange) +
             (price_banana * qty_banana) + (strawberry_price * qty_strawberry))

print(f'{total_sum:.2f}')

