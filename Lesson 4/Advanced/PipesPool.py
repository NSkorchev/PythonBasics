# Read user input
V_pool = int(input())
p1 = int(input())
p2 = int(input())
H = float(input())
# Logic

p1_debit = p1 * H
p2_debit = p2 * H
pool_current = p1_debit + p2_debit

pool_percent = pool_current / V_pool * 100

if V_pool >= pool_current:
    print(f"The pool is {pool_percent:.2f}% full. Pipe 1: {p1_debit / pool_current * 100:.2f}%.\
Pipe 2: {p2_debit / pool_current * 100:.2f}%.")
else:
    print(f"For {H} hours the pool overflows with {pool_current - V_pool:.2f} liters.")
# Output
