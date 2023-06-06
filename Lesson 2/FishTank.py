# Read user input
length = int(input())
width = int(input())
height = int(input())
percent = int(input()) / 100
# Logic
volume = length * width * height / 1000
liters = volume - volume * percent
# Output
print(liters)
