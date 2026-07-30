PROTECTIVE_NYLON = 1.50
PAINT = 14.50
PAINT_THINNER = 5.00
BAGS_PRICE = 0.4

needed_nylon = int(input())
needed_pain = int(input())
needed_thinner = int(input())
hours_for_done_working = int(input())

needed_nylon += 2
needed_pain += (needed_pain * 0.1)

sum_materials = (needed_nylon * PROTECTIVE_NYLON) + (needed_pain * PAINT) + (needed_thinner * PAINT_THINNER) + BAGS_PRICE
sum_workers = (sum_materials * 0.3) * hours_for_done_working
total_sum = sum_materials + sum_workers

print(total_sum)
