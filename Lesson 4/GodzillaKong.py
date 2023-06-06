# Read user input
movie_budget = float(input())
extras_count = int(input())
costume_price = float(input())

decor = 0.1 * movie_budget

if extras_count > 150:
    costume_price *= 0.9

total_price = costume_price * extras_count + decor
# Logic

if total_price > movie_budget:
    print(f"Not enough money!\nWingard needs {total_price - movie_budget:.2f} leva more.")
else:
    print(f"Action!\nWingard starts filming with {movie_budget - total_price:.2f} leva left.")
# Output
