length = int(input())
width = int(input())
height = int(input())
persent = float(input()) / 100

aquarium_volume = length * width * height
volume_liters = aquarium_volume / 1000
needed_liters = volume_liters - (volume_liters * persent)
print(needed_liters)