# Read user input
import exercise.request, exercise.parse, exercise.error

fhand = exercise.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
# Logic

# Output
