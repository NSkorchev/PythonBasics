# Read user input
hour = int(input())
day = input()
# Logic

if 18 >= hour >= 10:
    if day != 'Sunday':
        print('open')
    else:
        print('closed')
else:
    print('closed')

# Output
