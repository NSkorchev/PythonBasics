# Read user input
season = input()
km = float(input())
price = 0

# Logic
if 10000 < km <= 20000:
    price = 1.45 * km

if season == 'Spring' or season == 'Autumn':
    if km <= 5000:
        price = 0.75 * km
    elif 5000 < km <= 10000:
        price = 0.95 * km

elif season == 'Summer':
    if km <= 5000:
        price = 0.9 * km
    elif 5000 < km <= 10000:
        price = 1.1 * km

elif season == 'Winter':
    if km <= 5000:
        price = 1.05 * km
    elif 5000 < km <= 10000:
        price = 1.25 * km

# Output
print(f"{4* price * 0.9:.2f}")
