# Read user input
x = float(input())
y = float(input())
h = float(input())
# Logic
roof = (2 * x * y) + (x * h)
walls = (2 * (x * x) - 2.4 ) + (2 * x * y - 4.5)
green_paint = walls / 3.4
red_paint = roof / 4.3
# Output

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")

