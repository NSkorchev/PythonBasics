# # Read user input
# num = 0
# # Logic
# while True:
#     num += 1
#     if num % 3 == 0:
#         continue
#     print(num)
#     if num > 100:
#         break
# # Output
bigger_num = int(input())

while True:
    user_input = input()
    if user_input == "Stop":
        break
    num = int(user_input)
    if num > bigger_num:
        bigger_num = num
print(bigger_num)