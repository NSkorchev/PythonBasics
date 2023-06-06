# Read user input
name = input("Enter file:")

if len(name) < 1:
    name = "mbox.txt"
handle = open(name)
counts = dict()
bigcount = None
bigword = None

# Logic
for line in handle:
    if line.startswith("From:") or not line.startswith("From"):
        continue
    w = line.split()
    email = w[1]
    counts[email] = counts.get(email,0) + 1
    continue

for email, count in counts.items():
      if bigcount is None or count > bigcount:
          bigword = email
          bigcount = count

# Output
print(bigword, bigcount)



