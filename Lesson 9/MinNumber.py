# Read user input
min_num = int(input())

# Logic
while True:
    user_input = input()
    if user_input == "Stop":
        break
    num = int(user_input)
    if num < min_num:
        min_num = num

# Output
print(min_num)
