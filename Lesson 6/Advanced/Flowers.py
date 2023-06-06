# Read user input
hrizantemi_count = int(input())
roses_count = int(input())
tulip_count = int(input())
season = input()
holiday = input()
total_price = 0.00

# Logic
if season == 'Spring' or season == 'Summer':
    total_price = 2.00 * hrizantemi_count + 4.10 * roses_count + 2.50 * tulip_count

    if tulip_count > 7 and season == "Spring":
        total_price *= 0.95

elif season == 'Autumn' or season == 'Winter':
    total_price = 3.75 * hrizantemi_count + 4.50 * roses_count + 4.15 * tulip_count

    if roses_count >= 10 and season == "Winter":
        total_price *= 0.9

if (tulip_count + roses_count + hrizantemi_count) > 20:
    total_price *= 0.8

if holiday == 'Y':
    total_price *= 1.15

# Output
print(f"{total_price + 2:.2f}")
