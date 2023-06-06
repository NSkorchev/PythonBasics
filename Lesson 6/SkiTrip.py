# Read user input
days = int(input())
type_room = input()
review = input()
# Logic
price = 0.00
if type_room == 'room for one person':
    price = 18.00 * (days - 1)

elif type_room == 'apartment':
    price = 25.00 * (days - 1)

    if days <= 10:
        price *= 0.7
    elif 10 < days <= 15:
        price *= 0.65
    else:
        price *= 0.5

elif type_room == 'president apartment':
    price = 35.00 * (days - 1)

    if days <= 10:
        price *= 0.9
    elif 10 < days <= 15:
        price *= 0.85
    else:
        price *= 0.8

if review == 'positive':
    price *= 1.25
else:
    price *= 0.9
# Output
print(f"{price:.2f}")
