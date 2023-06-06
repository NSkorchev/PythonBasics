# Read user input
input_count = int(input())
sum_even = 0
sum_odd = 0

# Logic
for i in range(0, input_count):
    num = int(input())
    if i % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

# Output
if sum_even == sum_odd:
    print(f"Yes\nSum = {abs(sum_even)}")
else:
    print(f"No\nDiff = {abs(sum_even - sum_odd)}")