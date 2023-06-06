# Read user input
first_digit_limit = int(input())
second_digit_limit = int(input())
third_digit_limit = int(input())

# Logic
for i in range(2, first_digit_limit + 1, 2):
    for j in range(2, second_digit_limit + 1):
        for k in range(2, third_digit_limit + 1, 2):
            if j == 2 or j == 3 or j == 5 or j == 7:
                print(f'{i} {j} {k}')
# Output
