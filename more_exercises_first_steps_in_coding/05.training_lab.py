hall_wight = float(input())
hall_hight = float(input())

CORRIDOR = 1.0
DESC_HIGHT = 0.7
DESC_WIGHT = 1.2
LOST_WORK_SPASE = 3

hall_hight -= CORRIDOR
hall_hight //= DESC_HIGHT
hall_wight //= DESC_WIGHT

hall_sum = (hall_hight * hall_wight) - LOST_WORK_SPASE

print(hall_sum)
