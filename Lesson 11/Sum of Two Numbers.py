# Read user input
num1 = int(input())
num2 = int(input())
magick_num = int(input())
counter = 0
is_found = False
# Logic
for i in range(num1, num2 + 1):
    if is_found:
        break
    for j in range(num1, num2 + 1):
        counter += 1
        if magick_num == i + j:
            print(f"Combination N:{counter} ({i} + {j} = {magick_num})")
            is_found = True
            break
if not is_found:
    print(f"{counter} combinations - neither equals {magick_num}")





# Output
