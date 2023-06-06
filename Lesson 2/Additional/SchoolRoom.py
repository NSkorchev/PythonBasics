# Read user input
length = float(input()) * 100
width = float(input()) * 100 - 100

work_place_length =  120
work_place_width = 70

entrance = 1
desk = 2

# Logic

work_place = (length // work_place_length) * (width // work_place_width) - 3

# Output

print(work_place)
