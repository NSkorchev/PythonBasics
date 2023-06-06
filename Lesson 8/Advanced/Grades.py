# Read user input
students = int(input())
top_students = 0
avg_student = 0
poor_student = 0
failed_student = 0
avg_grade = 0
counter = 0
# Logic

for i in range(students):
    grade = float(input())
    counter += grade
    if grade >= 5.00:
        top_students += 1
    if 4.99 >= grade >= 4.00:
        avg_student += 1
    if 3.99 >= grade >= 3.00:
        poor_student += 1
    if grade < 3.00:
        failed_student += 1
    avg_grade = counter / students

print(f"Top students: {top_students / students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {avg_student / students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {poor_student / students * 100:.2f}%")
print(f"Fail: {failed_student / students * 100:.2f}%")
print(f"Average: {avg_grade:.2f}")


# Output
