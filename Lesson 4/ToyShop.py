# Read user input
excursion_price = float(input())

puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minion_count = int(input())
trucks_count = int(input())

puzzle_price = 2.60
dolls_price = 3.00
bears_price = 4.10
minion_price = 8.20
truck_price = 2.00

total_toys_count = puzzles_count + dolls_count + bears_count + minion_count + trucks_count
total_price = (puzzle_price * puzzles_count) + (dolls_price * dolls_count) + \
              (bears_price * bears_count) + (minion_price * minion_count) + \
              (truck_price * trucks_count)
# Logic

if total_toys_count >= 50:
    total_price *= 0.75

total_price *= 0.90

if total_price >= excursion_price:
    print(f"Yes! {total_price - excursion_price:.2f} lv left.")
else:
    print(f"Not enough money! {excursion_price - total_price:.2f} lv needed.")

# Output
