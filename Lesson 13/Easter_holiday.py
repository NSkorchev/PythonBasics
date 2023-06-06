# Read user input
destination = input()
dates = input()
nights_spend = int(input())
room_price = 0
# Logic
if dates == "21-23":
    if destination == "France":
        room_price = 30
    elif destination == "Italy":
        room_price = 28
    else:
        room_price = 32
elif dates == "24-27":
    if destination == "France":
        room_price = 35
    elif destination == "Italy":
        room_price = 32
    else:
        room_price = 37
else:
    if destination == "France":
        room_price = 40
    elif destination == "Italy":
        room_price = 39
    else:
        room_price = 43
# Output
print(f"Easter trip to {destination} : {nights_spend * room_price:.2f} leva.")