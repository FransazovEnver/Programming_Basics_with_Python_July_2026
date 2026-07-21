ONE_EURO = 1.94

price_of_vegetable = float(input())
price_of_fruit = float(input())
sum_vegetable = int(input())
sum_fruit = int(input())

vegetables = price_of_vegetable * sum_vegetable
fruits = price_of_fruit * sum_fruit
sum = (vegetables + fruits) / ONE_EURO
print(f'{sum:.2f}')
