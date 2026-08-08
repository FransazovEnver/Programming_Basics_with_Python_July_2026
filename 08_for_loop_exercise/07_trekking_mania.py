number_groups = int(input())

musala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

for _ in range(number_groups):
    people_count = int(input())

    if people_count <= 5:
        musala_count += people_count

    elif 6 <= people_count <= 12:
        monblan_count += people_count

    elif 13 <= people_count <= 25:
        kilimanjaro_count += people_count

    elif 26 <= people_count <= 40:
        k2_count += people_count

    else:
        everest_count += people_count


total_count = musala_count + monblan_count + kilimanjaro_count + k2_count + everest_count

print(f'{musala_count / total_count * 100:.2f}%')
print(f'{monblan_count / total_count * 100:.2f}%')
print(f'{kilimanjaro_count / total_count * 100:.2f}%')
print(f'{k2_count / total_count * 100:.2f}%')
print(f'{everest_count / total_count * 100:.2f}%')