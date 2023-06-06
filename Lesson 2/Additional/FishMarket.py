from math import floor
# Read user input
skumria_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
mussels_kg = int(input())
palamud_price = skumria_price * 1.6
safrid_price = caca_price * 1.8
mussels_price = 7.50
# Logic

total_price = (palamud_kg * palamud_price) + (safrid_kg * safrid_price) + (mussels_price * mussels_kg)


# Output
print(f"{total_price:.2f}")