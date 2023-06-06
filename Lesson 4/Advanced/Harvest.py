from math import ceil,floor
# Read user input
wineyard = int(input())
grape = float(input())
wine = int(input())
workers = int(input())

# Logic
grape_for_wine = 0.4 * wineyard * grape / 2.5
wine_left = grape_for_wine - wine

# Output
if grape_for_wine >= wine:
    print(f"Good harvest this year! Total wine: {grape_for_wine:.0f} liters.\n\
{ceil(wine_left)} liters left -> {ceil(wine_left / workers)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(wine - grape_for_wine)} liters wine needed.")
