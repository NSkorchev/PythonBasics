# Read user input
amount = int(input())
card = 0
cash = 0
counter = 0
transactions = 0
transactions_card = 0
fail = False

# Logic
while amount >= 0:
    sales = input()
    counter += 1

    if sales == "End":
        fail = True
        print(f"Failed to collect required money for charity.")
        break

    sales = int(sales)
    if counter % 2 == 1:
        if sales >= 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            cash += sales
            amount -= sales
            transactions += 1

    elif counter % 2 == 0:
        if sales <= 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            card += sales
            amount -= sales
            transactions_card += 1
# Output
if fail == False:
    print(f"Average CS: {cash / transactions:.2f}")
    print(f"Average CC: {card / transactions_card:.2f}")
