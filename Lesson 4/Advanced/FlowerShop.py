import math
# Read user input
magnolii = int(input())
zymbyli = int(input())
rozi = int(input())
cactus = int(input())
gift_price = float(input())
# Logic
magnolii_price = magnolii * 3.25
zymbyli_price = zymbyli * 4
rozi_price = rozi * 3.5
cactus_price = cactus * 8

total_price = (magnolii_price + zymbyli_price + rozi_price + cactus_price) * 0.95

# Output

if gift_price <= total_price:
    print(f"She is left with {math.floor(total_price - gift_price)} leva.")
else:
    print(f"She will have to borrow {math.ceil(gift_price - total_price)} leva.")