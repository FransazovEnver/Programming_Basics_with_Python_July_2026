n = int(input())

counter = 0
is_number = False

for row in range(1 ,n + 1):
    for _ in range(row):
        counter += 1
        print(counter, end=' ')

        if counter == n:
            is_number = True
            break

    if is_number:
        break

    print()
