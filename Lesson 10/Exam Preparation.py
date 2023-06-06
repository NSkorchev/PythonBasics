# Read user input
poor_grades = int(input())

problem_count = 0
poor_grades_count = 0
grades_sum = 0
last_problem = ""
has_failed = True
# Logic

while poor_grades_count < poor_grades:
    problem = input()
    has_failed = True
    problem_count += 1
    if problem == "Enough":
        problem_count -= 1
        has_failed = False
        break

    grade = int(input())
    grades_sum += grade
    if grade <= 4:
        poor_grades_count += 1
    last_problem = problem


# Output
if has_failed == False:
    print(f"Average score: {grades_sum / problem_count:.2f}")
    print(f"Number of problems: {problem_count}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {poor_grades} poor grades.")