# Read user input
# Use words.txt as the file name
fname = input("Enter file name: ")

# Logic
fh = open(fname)
inp = fh.read().upper().rstrip()

# Output
print(inp)