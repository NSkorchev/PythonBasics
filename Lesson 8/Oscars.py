# Read user input
actor_name = input()
academy_points = float(input())
n = int(input())
judges_points = 0.00
# Logic
for i in range(0, n):
    judge_name = input()
    judge_points = float(input())
    academy_points += (len(judge_name) * judge_points / 2)
    if academy_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {1250.5 - academy_points:.1f} more!")
# Output
