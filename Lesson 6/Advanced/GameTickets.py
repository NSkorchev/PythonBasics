# Read user input
budget = float(input())
category = input()
people = int(input())
# Logic

ticket_price = 0

if category == 'VIP':
    ticket_price = 499.99 * people
    if 1 <= people <= 4:
        budget *= 0.25
    elif 5 <= people <= 9:
        budget *= 0.4
    elif 10 <= people <= 24:
        budget *= 0.5
    elif 25 <= people <= 49:
        budget *= 0.6
    elif 50 <= people:
        budget *= 0.75
elif category == 'Normal':
    ticket_price = 249.99 * people
    if 1 <= people <= 4:
        budget *= 0.25
    elif 5 <= people <= 9:
        budget *= 0.4
    elif 10 <= people <= 24:
        budget *= 0.5
    elif 25 <= people <= 49:
        budget *= 0.6
    elif 50 <= people:
        budget *= 0.75

if budget >= ticket_price:
    print(f"Yes! You have {budget - ticket_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {ticket_price - budget:.2f} leva.")

# Output
