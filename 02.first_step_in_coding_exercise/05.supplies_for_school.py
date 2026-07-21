PENS_PACKS = 5.80
MARKERS_PACKS = 7.20
CLEANER = 1.20

numbers_of_pens = int(input())
numbers_of_markers = int(input())
board_cleaner_in_liter = int(input())
discount = int(input()) / 100

sum_of_all_products = (numbers_of_pens * PENS_PACKS) + (numbers_of_markers * MARKERS_PACKS) + (board_cleaner_in_liter * CLEANER)
sum_of_all_products -= (sum_of_all_products * discount)
print(sum_of_all_products)

