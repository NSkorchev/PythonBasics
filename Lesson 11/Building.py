# Read user input
floors = int(input())
rooms = int(input())
# Logic

for i in range(floors, 0, -1):
    for k in range(0, rooms):
        if i == floors:
            print(f"L{i}{k} ", end='')
            continue
        if i % 2 != 0:
            print(f"A{i}{k} ", end='')
        else:
            print(f"O{i}{k} ", end='')

# Output
    print('')





