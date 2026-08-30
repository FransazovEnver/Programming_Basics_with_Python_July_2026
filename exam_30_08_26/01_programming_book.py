PAGES = 899
COVER = 2

price_one_page = float(input())
price_one_cover = float(input())
amount_paint_paper = int(input()) / 100
price_designer = float(input())
sum_amount_team = int(input()) / 100


staring_sum = (price_one_page * PAGES) + (price_one_cover * COVER)
amount = staring_sum - (staring_sum * amount_paint_paper)
designer_sum = amount + price_designer
money = designer_sum - (designer_sum * sum_amount_team)

print(f'Avtonom should pay {money:.2f} BGN.')
