# Read user input
budget = float(input())
season = input()
location = ""
place = ""
# Logic
if season == "Summer":
    location = "Alaska"
elif season == "Winter":
    location = "Morocco"

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        budget *= 0.65
    elif season == "Winter":
        budget *= 0.45

elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        budget *= 0.8
    elif season == "Winter":
        budget *= 0.6

elif budget > 3000:
    place = "Hotel"
    budget *= 0.9
# Output

print(f"{location} - {place} - {budget:.2f}")

