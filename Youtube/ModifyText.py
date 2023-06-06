# Read user input
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lines = 0
average = 0

# Logic
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        lines += 1
        y = line.find('0.')
        z = line[y:]
        num = float(z)
        average += float(z)

# Output
print(f"Average spam confidence: {average / lines}")