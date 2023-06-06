# Read user input
customers = int(input())
item = 0
money_spend = 0
total = 0
# Logic
for i in range(customers):
    Finish = True
    item = 0
    while Finish:
        purchase = input()

        if purchase == "basket":
            total += 1.50
        elif purchase == "wreath":
            total += 3.80
        elif purchase == "chocolate bunny":
            total += 7.00

        if purchase == "Finish":
            if item % 2 == 0:
                total = 0.8 * total
            money_spend += total
            print(f"You purchased {item} items for {total:.2f} leva.")
            total = 0
            item = 0
            Finish = False
            break
        item += 1

# Output
print(f"Average bill per client is: {money_spend / customers:.2f} leva.")
