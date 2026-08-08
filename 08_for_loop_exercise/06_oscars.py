MIN_POINTS = 1250.5

actor_name = input()
point_academy = float(input())
numbers_judges = int(input())


for _ in range(numbers_judges):
    judge_name = input()
    judge_points = float(input())

    point_academy += (len(judge_name) * judge_points / 2)



    if point_academy > MIN_POINTS:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {point_academy:.1f}!')
        break


else:
    print(f'Sorry, {actor_name} you need {MIN_POINTS - point_academy:.1f} more!')

