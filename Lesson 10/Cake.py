# Read user input
cake_lenght = int(input())
cake_width = int(input())
cake_size = cake_width * cake_lenght
cake_peace = ""
# Logic

while cake_size > 0:
    cake_peace = input()
    if cake_peace != "STOP":
        cake_size -= int(cake_peace)
    else:
        print(f"{cake_size} pieces are left.")
        break
    if cake_size <= 0:
        print(f"No more cake left! You need {abs(cake_size)} pieces more.")
        break

# Output
