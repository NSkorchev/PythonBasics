import math
# Read user input
tournaments = int(input())
points = int(input())
tournament_points = 0
win = 0

# Logic
for i in range(0, tournaments):
    progress = input()
    if progress == "W":
        tournament_points += 2000
        win += 1
    elif progress == "F":
        tournament_points += 1200
    elif progress == "SF":
        tournament_points += 720

# Output
print(f"Final points: {points + tournament_points}")
print(f"Average points: {math.floor(tournament_points / tournaments)}")
print(f"{win / tournaments * 100:.2f}%")