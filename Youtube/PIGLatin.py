# Read user input
original = input("Enter a word: ")
word = original.lower()
first = word[0]
second = word[1]
third = word[2]
pyg = 'ay'
new_word = word + pyg + first
new_word = new_word[1:len(new_word)]
# Logic
if len(word) > 0 and word.isalpha():
    print(new_word)
else:
    print('empty')
# Output
