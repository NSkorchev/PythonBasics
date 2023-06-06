# Read user input
heritage = float(input())
year = int(input())
money = False
counter = 0
# Logic

for i in range(1800, year + 1):
    counter += 1
    if i % 2 == 0:
        heritage -= 12000
    else:
        heritage -= 12000 + 50 * (counter + 17)

    if heritage < 0 and i == year:
        print(f"He will need {abs(heritage):.2f} dollars to survive.")
        money = True
        break

# Output
if not money:
    print(f"Yes! He will live a carefree life and will have {heritage:.2f} dollars left.")
