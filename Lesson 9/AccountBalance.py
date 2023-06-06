# Read user input
balance = 0

# Logic

while True:
    user_input = input()
    if user_input == 'NoMoreMoney':
        break
    deposit = float(user_input)
    if deposit < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {deposit:.2f}")
    balance += deposit

# Output
print(f"Total: {balance:.2f}")