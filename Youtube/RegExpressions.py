import re
# Read user input
name = input("Enter file:")
result = 0
if len(name) < 1:
    name = "dataFiles"
handle = open(name)
numbers = list()

# Logic
for line in handle:
    line = line.rstrip()
    y = re.findall('([0-9]+)',line)
    if len(y) == 0:
        continue
    else:
        for i in y:
            result += int(i)
            numbers.append(i)

# Output
print(result)
print(len(numbers))