# Read user input
num1 = int(input())
num2 = int(input())
num3 = 0
# Logic

for i in range(num1, num2 + 1):
    for j in range(1, i):
        num1 += 1
        print(num1)
    if num1 == num2:
        break





# Output
