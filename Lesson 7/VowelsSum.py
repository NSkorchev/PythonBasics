# Read user input
text = input()
string_lenght = len(text)
# Logic
result = 0

for i in range(0, string_lenght):
    if text[i] == 'a':
        result += 1
    elif text[i] == 'e':
        result += 2
    elif text[i] == 'i':
        result += 3
    elif text[i] == 'o':
        result += 4
    elif text[i] == 'u':
        result += 5

print(result)
# Output
