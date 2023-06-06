# Read user input
juniors = int(input())
seniors = int(input())
track = input()
# Logic

fee = 0.00
participants = seniors + juniors

if track == 'trail':
    fee = 5.5 * juniors + 7 * seniors
elif track == 'downhill':
    fee = 12.25 * juniors + 13.75 * seniors
elif track == 'road':
    fee = 20 * juniors + 21.5 * seniors
elif track == 'cross-country':
    fee = 8 * juniors + 9.5 * seniors

    if participants >= 50:
        fee *= 0.75
# Output

print(f"{fee * 0.95:.2f}")