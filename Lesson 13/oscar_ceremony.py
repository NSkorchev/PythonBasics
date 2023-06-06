# Read user input
room_rent = int(input())
# Logic
oscars = 0.7 * room_rent
serving = 0.85 * oscars
sound = 0.5 * serving
expenses = oscars + sound + serving + room_rent
# Output
print(f'{expenses:.2f}')
