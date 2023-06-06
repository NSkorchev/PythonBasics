# Read user input
letter = ""
word = ""
cCount = 0
oCount = 0
nCount = 0
secretWordCount = 0

# Logic
while letter != "End":
    letter = input()
    isFirstSecretLetter = False

    if not letter.isalpha():
        isFirstSecretLetter = True

    if letter == "c" and cCount < 1:
        cCount += 1
        secretWordCount += 1
        isFirstSecretLetter = True
    elif letter == "o" and oCount < 1:
        oCount += 1
        secretWordCount += 1
        isFirstSecretLetter = True
    elif letter == "n" and nCount < 1:
        nCount += 1
        secretWordCount += 1
        isFirstSecretLetter = True

    if secretWordCount == 3:
        print(f"{word}", end=' ')
        secretWordCount = 0
        cCount = 0
        oCount = 0
        nCount = 0
        word = ""
    elif not isFirstSecretLetter:
        word += str(letter)
# Output
