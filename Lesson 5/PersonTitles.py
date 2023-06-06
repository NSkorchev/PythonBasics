# Read user input
age = float(input())
sex = input()
# Logic

if sex == 'f':
    if age >= 16:
        print("Ms.")
    else:
        print('Miss')
elif sex == 'm':
    if age >= 16:
        print('Mr.')
    else:
        print('Master')
else:
    print('error')
# Output
