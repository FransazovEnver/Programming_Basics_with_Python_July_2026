annual_training_tax = int(input())

basketball_shoes = annual_training_tax - (annual_training_tax * 0.40)
basketball_team = basketball_shoes - (basketball_shoes * 0.20)
basket_ball = basketball_team * 0.25
basketball_access = basket_ball * 0.20

sum_basketball = annual_training_tax + basketball_shoes + basketball_team + basket_ball + basketball_access
print(sum_basketball)