# Read user input
pwd = 'cici'
# Logic
for char_1 in range(97, 123):
    for char_2 in range(97, 123):
        for char_3 in range(97, 123):
            for char_4 in range(97, 123):

                word = f'{chr(char_1)}{chr(char_2)}{chr(char_3)}{chr(char_4)}'
                if word == pwd:
                    print('Pass found!')
                    print(word)


# Output
