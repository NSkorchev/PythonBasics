# Read user input
current_name = None
current_goals = -1
# Logic

while current_goals < 10:
    player_name = input()

    if player_name == "END":
        break

    goal_scored = int(input())

    if goal_scored > current_goals:
        current_name = player_name
        current_goals = goal_scored


# Output
print(f"{current_name} is the best player!")
if current_goals >= 3:
    print(f"He has scored {current_goals} goals and made a hat-trick !!!")
else:
     print(f"He has scored {current_goals} goals.")