import sys
# Read user input
input_count = int(input())
max_number = -sys.maxsize
sum_numbers = 0
# Logic
for i in range(0, input_count):
    num = int(input())
    if num > max_number:
        max_number = num

    sum_numbers += num

if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {sum_numbers - max_number}")
else:
    print("No")
    sum_numbers = sum_numbers - max_number
    print(f"Diff = {abs(max_number - sum_numbers)}")

# Output
