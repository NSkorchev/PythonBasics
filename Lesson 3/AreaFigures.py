import math
# Read user input
figure = input()

# Logic

# if figure == "square":
#     pass
# elif figure == "circle":
#     pass
# elif figure == "triangle":
#     pass
# elif figure == "rectangle":
#     pass
# else:
#     print("square, circle, tringle or rectangle")

if figure == "square":
    side = float(input())
    area = side * side
    print(figure)
    print(f"{area:.3f}")
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_b * side_a
    print(figure)
    print(f"{area:.3f}")
elif figure == "triangle":
    c = float(input())
    h = float(input())
    area = c * h / 2
    print(figure)
    print(f"{area:.3f}")
elif figure == "circle":
    r = float(input())
    area = math.pi * r * r
    print(figure)
    print(f"{area:.3f}")
else:
    print("square, circle, tringle or rectangle")
# Output
