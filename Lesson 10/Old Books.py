# Read user input
book = input()
count = 0
# Logic
while True:
    book_title_1 = input()
    count += 1

    if book_title_1 == book:
        count -= 1
        print(f"You checked {count} books and found it.")
        break

    if book == "No More Books" or book_title_1 == "No More Books":
        count -= 1
        print(f"The book you search is not here!")
        print(f"You checked {count} books.")
        break
# Output
