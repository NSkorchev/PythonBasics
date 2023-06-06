# Read user input
season = input()
group_type = input()
students = int(input())
nights = int(input())
price_per_night = 0
sport = ""

# Logic
if season == "Winter":

    if group_type == "boys":
        price_per_night = 9.6
        sport = "Judo"
    elif group_type == "girls":
        price_per_night = 9.6
        sport = "Gymnastics"
    else:
        price_per_night = 10
        sport = "Ski"

elif season == "Spring":

    if group_type == "boys":
        price_per_night = 7.2
        sport = "Tennis"
    elif group_type == "girls":
        price_per_night = 7.2
        sport = "Athletics"
    else:
        price_per_night = 9.5
        sport = "Cycling"

elif season == "Summer":

    if group_type == "boys":
        price_per_night = 15
        sport = "Football"
    elif group_type == "girls":
        price_per_night = 15
        sport = "Volleyball"
    else:
        price_per_night = 20
        sport = "Swimming"

price = price_per_night * nights * students

if students >= 50:
    price *= 0.5
elif 50 > students >= 20:
    price *= 0.85
elif 10 <= students < 20:
    price *= 0.95

# Output
print(f"{sport} {price:.2f} lv.")
