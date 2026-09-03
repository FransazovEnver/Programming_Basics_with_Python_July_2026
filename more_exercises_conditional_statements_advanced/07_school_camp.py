season = input()
type_group = input()
number_students = int(input())
number_night = int(input())

price = 0
sport = ""

if season == "Winter":
    if type_group == "boys" or type_group == "girls":
        price = 9.60
    elif type_group == "mixed":
        price = 10
elif season == "Spring":
    if type_group == "boys" or type_group == "girls":
        price = 7.20
    elif type_group == "mixed":
        price = 9.50
elif season == "Summer":
    if type_group == "boys" or type_group == "girls":
        price = 15
    elif type_group == "mixed":
        price = 20

if season == "Winter":
    if type_group == "girls":
        sport = "Gymnastics"
    elif type_group == "boys":
        sport = "Judo"
    elif type_group == "mixed":
        sport = "Ski"
elif season == "Spring":
    if type_group == "girls":
        sport = "Athletics"
    elif type_group == "boys":
        sport = "Tennis"
    elif type_group == "mixed":
        sport = "Cycling"
elif season == "Summer":
    if type_group == "girls":
        sport = "Volleyball"
    elif type_group == "boys":
        sport = "Football"
    elif type_group == "mixed":
        sport = "Swimming"