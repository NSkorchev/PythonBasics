import math
# Read user input
end_of_words = True
most_powerful_word = ''
powerful_word_weight = 0
# Logic
while end_of_words:
    word = input()
    if word == "End o words":
        end_of_words = False
        break
    weight = 0
    for i in range(0, len(word)):
        weight += ord(word[i])
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'y' \
            or word[0] == 'A' or word[0] == 'E' or word[0] == 'I' or word[0] == 'U' or word[0] == 'O' or word[0] == 'Y':
        weight *= len(word)
    else:
        weight /= len(word)

    if weight > powerful_word_weight:
        most_powerful_word = word
        weight = powerful_word_weight
# Output
print(f"The most powerful word is {most_powerful_word} - {powerful_word_weight}")

