# Read user input
username = input()
password = input()
# Logic
input_password = input()
fail_count = 0

while password != input_password:
    input_password = input()
    fail_count += 1
    if fail_count > 4:
        print("Too many wrong attempts!")
        break

print(f"Welcome {username}!")

# Output
