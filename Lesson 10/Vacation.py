# Read user input
budget_vacation = float(input())
savings = float(input())
spend_count = 0
days = 0


# Logic
while spend_count < 5:
    if savings >= budget_vacation:
        print(f"You saved the money for {days} days.")
        break

    activity = input()
    amount = float(input())
    days += 1

    if activity == "spend":
        spend_count += 1
        savings -= amount
        if savings < 0:
            savings = 0
    elif activity == "save":
        spend_count = 0
        savings += amount

else:
    print("You can't save the money.")
    print(f"{days}")
# Output
