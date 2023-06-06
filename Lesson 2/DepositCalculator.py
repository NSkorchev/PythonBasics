# Read user input
deposit = float(input())
period = int(input())
yearly_yield = float(input()) / 100
# Logic

total = deposit + period * ((deposit * yearly_yield ) / 12)

# Output

print(total)