# Read user input
colored_eggs = int(input())
red = 0
green = 0
blue = 0
orange = 0
Max_eggs = 0
# Logic

for i in range(colored_eggs):
    color = input()
    if color == "red":
        red += 1
    elif color == "green":
        green += 1
    elif color == "blue":
        blue += 1
    else:
        orange += 1


if red > green and red > orange and red > blue:
    Max_eggs = red
    color = "red"
elif orange > red and orange > blue and orange > green:
    Max_eggs = orange
    color = "orange"
elif blue > orange and blue > red and blue > green:
    Max_eggs = blue
    color = "blue"
else:
    Max_eggs = green
    color = "green"

# Output
print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {Max_eggs} -> {color}")



