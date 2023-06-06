# Read user input
dancer_count = int(input())
points = float(input())
season = input()
place = input()
money = 0

# Logic
if place == "Bulgaria":
    money = points * dancer_count
    if season == "summer":
        money *= 0.95
    elif season == "winter":
        money *= 0.92
elif place == "Abroad":
    money = points * dancer_count * 1.5
    if season == "summer":
        money *= 0.90
    elif season == "winter":
        money *= 0.85

donation = 0.75 * money
# Output
print(f'Charity - {donation:.2f}')
print(f'Money per dancer - {(money - donation) / dancer_count:.2f}')