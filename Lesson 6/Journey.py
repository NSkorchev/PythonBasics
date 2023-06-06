# Read user input
budget = float(input())
season = input()

destination = None
place = None
# Logic

if 0 < budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        place = 'Camp'
        budget *= 0.3
    elif season == 'winter':
        place = 'Hotel'
        budget *= 0.7
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        place = 'Camp'
        budget *= 0.4
    elif season == 'winter':
        place = 'Hotel'
        budget *= 0.8
elif budget >= 1000:
    place = 'Hotel'
    destination = 'Europe'
    budget *= 0.9
print(f"Somewhere in {destination}")
print(f"{place} - {budget:.2f}")


# Output
