# Read user input
fname = input("Enter file name: ")
fh = open(fname)
lst = list()

# Logic
for line in fh:
    line = line.rstrip()
    w = line.split()
    for i in w:
        if i not in lst:
            lst.append(i)
lst.sort()
# Output
print(lst)