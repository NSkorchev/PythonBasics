# Read user input
n = int(input())
time = input()
# Logic
taxi = 0
bus = 0
train = 0
if time == 'day':
    taxi = f"{0.7 + n * 0.79:.2f}"
    bus = f"{n * 0.09:.2f}"
    train = f"{n * 0.06:.2f}"
elif time == 'night':
    taxi = f"{0.7 + n * 0.9:.2f}"
    bus = f"{n * 0.09:.2f}"
    train = f"{n * 0.06:.2f}"
else:
    print("Wrong input!")

if 0 <= n < 20:
    print(f"{taxi}")
elif 100 > n >= 20:
    print(f"{bus}")
else:
    print(f"{train}")

# Output
