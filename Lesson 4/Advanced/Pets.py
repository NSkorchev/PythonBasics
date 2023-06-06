from math import ceil, floor
# Read user input
days = int(input())
food_left = int(input())
food_dog = float(input())
food_cat = float(input())
food_turtle = float(input()) / 1000
# Logic

food_total = days * (food_turtle + food_cat + food_dog)
if food_left >= food_total:
    print(f'{floor(food_left - food_total)} kilos of food left.')
else:
    print(f'{ceil(food_total - food_left)} more kilos of food are needed.')
# Output
