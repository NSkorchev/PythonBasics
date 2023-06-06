# Read user input
from curses.ascii import islower

fuel_type = input('')
liters_left = float(input())
while True:

    if fuel_type == 'Diesel' and liters_left >= 25:
        print(f"You have enough {fuel_type.lower()}.")
        break
    elif fuel_type == 'Diesel' and liters_left < 25:
        print(f"Fill your tank with {fuel_type.lower()}!")
        break
    elif fuel_type == 'Gasoline' and liters_left >= 25:
        print(f"You have enough {fuel_type.lower()}.")
        break
    elif fuel_type == 'Gasoline' and liters_left < 25:
        print(f"Fill your tank with {fuel_type.lower()}!")
        break
    elif fuel_type == 'Gas' and liters_left >= 25:
        print(f"You have enough {fuel_type.lower()}.")
        break
    elif fuel_type == 'Gas' and liters_left < 25:
        print(f"Fill your tank with {fuel_type.lower()}!")
        break

    else:
        print('Invalid fuel!')
        break
# Logig

# Output
