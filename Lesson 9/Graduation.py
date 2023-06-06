# Read user input
name = input()
grade = 0
fails = 0
current_class = 1
# Logic
while True:
    current_grade = float(input())
    if current_grade < 4:
        fails += 1
        if fails >= 2:
            break
        continue
    grade += current_grade
    current_class += 1

    if current_class > 12:
        break
# Output
if fails >= 2:
    print(f"{name} has been excluded at {current_class} grade")
else:
    average = grade / 12
    print(f"{name} graduated. Average grade: {average:.2f}")
