# Read user input

months = int(input())
water = 20.00
internet = 15.00
bills = 0
electricity_all = 0
other = 0
# Logic

for i in range(months):
    electricity = float(input())
    electricity_all += electricity
    other += (electricity + water + internet) * 1.20
# Output

print(f'Electricity: {electricity_all:.2f} lv')
print(f'Water: {water * months:.2f} lv')
print(f'Internet: {internet * months:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {(other + water * months + internet * months + electricity_all) / months:.2f} lv')
