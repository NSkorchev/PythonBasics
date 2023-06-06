# Read user input
budget = int(input())
season = input()
fisherman_count = int(input())

# Logic
boat_price = 0

if season == 'Spring':
    boat_price: float = 3000
    if fisherman_count <= 6:
        boat_price *= 0.9
    elif 7 <= fisherman_count <= 11:
        boat_price *= 0.85
    else:
        boat_price *= 0.75
    if fisherman_count % 2 == 0:
        boat_price *= 0.95
elif season == 'Summer':
    boat_price: float = 4200
    if fisherman_count <= 6:
        boat_price *= 0.9
    elif 7 <= fisherman_count <= 11:
        boat_price *= 0.85
    else:
        boat_price *= 0.75
    if fisherman_count % 2 == 0:
        boat_price *= 0.95
elif season == 'Autumn':
    boat_price: float = 4200
    if fisherman_count <= 6:
        boat_price *= 0.9
    elif 7 <= fisherman_count <= 11:
        boat_price *= 0.85
    else:
        boat_price *= 0.75
elif season == 'Winter':
    boat_price: float = 2600
    if fisherman_count <= 6:
        boat_price *= 0.9
    elif 7 <= fisherman_count <= 11:
        boat_price *= 0.85
    else:
        boat_price *= 0.75
    if fisherman_count % 2 == 0:
        boat_price *= 0.95

# Output
if budget >= boat_price:
    print(f"Yes! You have {budget - boat_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {boat_price - budget:.2f} leva.")
