# Read user input
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)


def computepay(h, r):
    if h < 40:
        p = h * r
    else:
        p = 40 * r + (h - 40) * r * 1.5
    return p


p = computepay(h, r)
print("Pay", p)

# Logic

# Output
