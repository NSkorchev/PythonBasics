# Read user input
import turtle
import random
pen = turtle.Pen()
# Logic
turtle.bgcolor('black')

for x in range(360):
    if x % 6 == 0:
        pen.pencolor('red')
    elif x % 6 ==1:
        pen.pencolor('purple')
    elif x % 6 ==2:
        pen.pencolor('green')
    elif x % 6 == 3:
        pen.pencolor('blue')
    elif x % 6 == 4:
        pen.pencolor('orange')
    elif x % 6 == 5:
        pen.pencolor('yellow')
    pen.width(x // 100 + 1)
    pen.forward(x)
    pen.left(59)

turtle.exitonclick()

# Output
