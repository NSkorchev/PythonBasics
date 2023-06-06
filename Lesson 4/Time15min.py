# Read user input
hours = int(input())
minutes = int(input()) + 15

# Logic
if minutes > 59:
    hours += 1
    minutes -= 60

if hours > 23:
    hours -= 24

# Output
if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")


