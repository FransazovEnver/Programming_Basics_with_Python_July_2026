pool_volume = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hour_worker_left = float(input())

sum_pipe_1 = pipe_1 * hour_worker_left
sum_pipe_2 = pipe_2 * hour_worker_left
sum_water = sum_pipe_1 + sum_pipe_2

if sum_water <= pool_volume:
    full_persent = sum_water / pool_volume * 100
    percent_pipe1 = sum_pipe_1 / sum_water * 100
    percent_pipe2 = sum_pipe_2 / sum_water * 100
    print(f"The pool is {full_persent:.2f}% full. "
          f"Pipe 1: {percent_pipe1:.2f}%. Pipe 2: "
          f"{percent_pipe2:.2f}%.")
else:
    water_left =  sum_water - pool_volume
    print(f"For {hour_worker_left:.2f} hours the pool overflows with "
            f"{water_left:.2f} liters.")
