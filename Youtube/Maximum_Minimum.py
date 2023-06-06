import sys
# Read user input
largest = -sys.maxsize
smallest = sys.maxsize

# Logic
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)
    except:
        print('Invalid input')
        continue
    if n > largest:
        largest = int(num)
    if n < smallest:
        smallest = int(num)


# Output
print("Maximum", largest)
print("Minimum", smallest)
