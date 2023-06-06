# Read user input

for digit_1 in range(10):
    for digit_2 in range(10):
        if digit_1 == digit_2:
            continue
        for digit_3 in range(10):
            if digit_2 == digit_3 or digit_1 == digit_3:
                continue
            for digit_4 in range(10):
                if digit_1 == digit_4 or digit_2 == digit_4 or digit_3 ==digit_4:
                    continue
                for digit_5 in range(10):
                    if digit_5 == digit_1 or digit_5 == digit_2 or digit_5 == digit_3 or digit_5 == digit_4:
                        continue
                    print(f'{digit_1}{digit_2}{digit_3}{digit_4}{digit_5}')

# Logic

# Output
