# Read user input
size = int(input())
current = 0
is_current_bigger_size = False
# Logic
for row in range(1, size + 1):
    for col in range(1, row + 1):
        current += 1
        if current > size:
            is_current_bigger_size = True
            break
        print(f'{current}', end=' ')
    if is_current_bigger_size:
        break
    print(f"")
# Output
