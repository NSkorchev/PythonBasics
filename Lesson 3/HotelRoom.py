# Read user input
month = input()
stay = int(input())
# Logic

studio_price: float = 0
apartment_price: float = 0
total = 0

if month == 'May' or month == 'October':
    studio_price = 50 * stay
    apartment_price = 65 * stay
    if 14 > stay > 7:
        studio_price *= 0.95
    elif stay > 14:
        studio_price *= 0.7
elif month == "June" or month == "September":
    studio_price = 75.2 * stay
    apartment_price = 68.7 * stay
    if stay > 14:
        studio_price *= 0.8
elif month == "July" or month == "August":
    studio_price = 76 * stay
    apartment_price = 77 * stay

if stay > 14:
    apartment_price *= 0.9

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
# Output
