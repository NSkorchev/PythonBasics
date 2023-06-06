# Read user input
moves = int(input())
score = 0
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

# Logic
for i in range(moves):
    number = int(input())

    if 0 <= number <= 9:
        score += 0.2 * number
        count0 += 1
    elif 10 <= number <= 19:
        score += 0.3 * number
        count1 += 1
    elif 20 <= number <= 29:
        score += 0.4 * number
        count2 += 1
    elif 30 <= number <= 39:
        score += 50
        count3 += 1
    elif 40 <= number <= 50:
        score += 100
        count4 += 1
    else:
        score /= 2
        count5 += 1
# Output
print(f'{score:.2f}')
print(f'From 0 to 9: {count0 / moves * 100:.2f}%')
print(f'From 10 to 19: {count1 / moves * 100:.2f}%')
print(f'From 20 to 29: {count2 / moves * 100:.2f}%')
print(f'From 30 to 39: {count3 / moves * 100:.2f}%')
print(f'From 40 to 50: {count4 / moves * 100:.2f}%')
print(f'Invalid numbers: {count5 / moves * 100:.2f}%')


