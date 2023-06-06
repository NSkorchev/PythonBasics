# Read user input

stadium_capacity = int(input())
fans_count = int(input())
fans_A = 0
fans_B = 0
fans_V = 0
fans_G = 0

# Logic

for i in range(fans_count):
    sector = input()
    if sector == "A":
        fans_A += 1
    elif sector == "B":
        fans_B += 1
    elif sector == "V":
        fans_V += 1
    elif sector == "G":
        fans_G += 1


# Output

print(f"{fans_A / fans_count * 100:.2f}%")
print(f"{fans_B / fans_count * 100:.2f}%")
print(f"{fans_V / fans_count * 100:.2f}%")
print(f"{fans_G / fans_count * 100:.2f}%")
print(f"{fans_count / stadium_capacity * 100:.2f}%")