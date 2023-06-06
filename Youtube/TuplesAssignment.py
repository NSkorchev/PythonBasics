# Read user input
name = input("Enter file:")
if len(name) < 1:
    name = "mbox.txt"
handle = open(name)
hours = dict()
x = dict()
# Logic
for line in handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    time = words[5]
    pieces = time.split(":")
    hour = pieces[0]
    hours[hour] = hours.get(hour, 0) + 1

# Output
for k,v in sorted(hours.items()):
    print(k,v)
# print(sorted((v,k) for v,k in hours.items()))

