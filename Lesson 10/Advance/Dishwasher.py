# Read user input
detergent = int(input()) * 750
dishes = 0
pots = 0
counter = 0

# Logic

while detergent >= 0:
    utensils = input()
    counter += 1

    if utensils == "End":
        break

    if counter % 3 == 0:
        pots += int(utensils)
        detergent -= int(utensils) * 15
    else:
        dishes += int(utensils)
        detergent -= int(utensils) * 5

# Output
if detergent >= 0:
    print(f"Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")
else:
    print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")


