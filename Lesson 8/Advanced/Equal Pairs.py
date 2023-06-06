from sys import maxsize
# Read user input

last_sum = -maxsize
max_diff = -maxsize

# Logic
for i in range(int(input())):
    num1 = int(input())
    num2 = int(input())
    pairs_sum = num1 + num2

    if i == 0:
        last_sum = pairs_sum
        continue

    if last_sum != pairs_sum:
        if abs(pairs_sum - last_sum) > max_diff:
            max_diff = abs(pairs_sum - last_sum)

    last_sum = pairs_sum
# Output

if max_diff == -maxsize:
    print(f"Yes, value={last_sum}")
else:
    print(f"No, maxdiff={max_diff}")