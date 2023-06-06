import sys
# Read user input
n = int(input())
counter = 0
# Logic
for x1 in range(0, n + 1):
    for x2 in range(0, n + 1):
        for x3 in range(0, n + 1):
            if n == x1 + x2 + x3:
                counter += 1

print(counter)

# Output
