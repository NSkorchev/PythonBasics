# Read user input
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox.txt"

fh = open(fname)
count = 0
lst = list()
email = ""

for line in fh:
    if line.startswith("From:"):
        continue
    elif line.startswith("From"):
        w = line.split()
        email = w[1]
        count += 1
        print(email)
    # lst.append(email)

# lst = list(dict.fromkeys(lst))
# print(lst, end = '')
print("There were", count, "lines in the file with From as the first word")

# Logic

# Output
