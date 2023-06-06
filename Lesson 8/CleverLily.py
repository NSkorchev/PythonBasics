# Read user input
age = int(input())
washing_machine = float(input())
toy_price = int(input())
toy_count = 0
savings = 0
money_given = 10
# Logic
for i in range(1, age + 1):
    if i % 2 == 0:
        savings += money_given - 1
        money_given += 10
    else:
        toy_count += 1
total_money = savings + toy_count * toy_price

if total_money >= washing_machine:
    print(f"Yes! {total_money - washing_machine:.2f}")
else:
    print(f"No! {washing_machine - total_money:.2f}")
# Output
