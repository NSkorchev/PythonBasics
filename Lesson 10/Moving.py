# Read user input
space_width = int(input())
space_length = int(input())
space_height = int(input())
boxes = ""
room_volume = space_height * space_length * space_width
# Logic

while room_volume > 0:
    boxes = input()
    if boxes != "Done":
        room_volume -= int(boxes)
    else:
        print(f"{room_volume} Cubic meters left.")
        break
else:
    print(f"No more free space! You need {abs(room_volume)} Cubic meters more.")

# Output
