# Read user input
input_count = int(input())
# Logic
result = 0
result_2 = 0

for i in range(0, input_count):
    num = int(input())
    result += num

for i in range(0, input_count):
    num = int(input())
    result_2 += num

if result == result_2:
    print(f"Yes, sum = {result}")
else:
    print(f"No, diff = {abs(result - result_2)}")
# Output
