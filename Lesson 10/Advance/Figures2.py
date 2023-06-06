# Read user input
import turtle
pen = turtle.Pen()
turtle.speed(1500)
# Logic
while True:
    direction = input("Enter direction (forward/backward/left/right):")
    if direction == "forward":
        pen.forward(100)
    if direction == "backward":
        pen.forward(100)
    if direction == "left":
        pen.left(90)
        pen.forward(100)
    if direction == "right":
        pen.right(90)
        pen.forward(100)
# Output
