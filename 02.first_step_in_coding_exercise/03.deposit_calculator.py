deposit_money = float(input())
deadline_date = int(input())
annual_interest_rate = float(input()) / 100

sum = deposit_money + deadline_date * ((deposit_money * annual_interest_rate) / 12)
print(sum)
