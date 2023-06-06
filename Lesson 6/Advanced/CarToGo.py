# Read user input
budget = float(input())
season = input()
car = ""
holiday_class = ""
# Logic

if season == "Summer":
    car = 'Cabrio'
else:
    car = 'Jeep'

if budget <= 100:
    holiday_class = "Economy class"

    if season == "Summer":
        budget *= 0.35
    elif season == "Winter":
        budget *= 0.65

elif 500 >= budget > 100:
    holiday_class = "Compact class"

    if season == "Summer":
        budget *= 0.45
    elif season == "Winter":
        budget *= 0.80

elif budget > 500:
    holiday_class = "Luxury class"
    budget *= 0.9
    car = 'Jeep'

# Output
print(f"{holiday_class}")
print(f"{car} - {budget:.2f}")