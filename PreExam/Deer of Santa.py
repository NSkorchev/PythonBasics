import math
# Read user input
days_gone = int(input())
food_kg = int(input())
first_deer_food = float(input())
second_deer_food = float(input())
third_deer_food = float(input())

# Logic
food_eaten = days_gone * (first_deer_food + second_deer_food + third_deer_food)

# Output
if food_kg >= food_eaten:
    print(f'{math.floor(food_kg - food_eaten)} kilos of food left.')
else:
    print(f'{math.ceil(food_eaten - food_kg)} more kilos of food are needed.')