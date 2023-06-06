# Read user input
money = 0
# Logic
while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    while True:
        savings = float(input())
        money += savings
        if money >= budget:
            print(f'Going to {destination}!')
            money = 0
            break
# Output
