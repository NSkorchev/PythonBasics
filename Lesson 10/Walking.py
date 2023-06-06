# Read user input
daily_steps = 0
steps_home = 0
goal = 10000
# Logic
while daily_steps < goal:
    steps = input()
    if steps != "Going home":
        daily_steps += int(steps)
    elif steps == "Going home":
        steps_home = int(input())
        daily_steps += steps_home
        if daily_steps < goal:
            print(f"{goal - daily_steps} more steps to reach goal.")
            break

else:
    print(f"Goal reached! Good job!")
    print(f"{daily_steps - goal} steps over the goal!")

# Output
