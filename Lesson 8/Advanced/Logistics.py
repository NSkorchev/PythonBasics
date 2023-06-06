# Read user input
loads = int(input())
price = 0
train = 0
microbus = 0
truck = 0
# Logic

for i in range(loads):
    load = int(input())

    if load <= 3:
        price += (200 * load)
        microbus += load
    if 4 <= load <= 11:
        price += (175 * load)
        truck += load
    if load >= 12:
        price += (120 * load)
        train += load
# Output
print(f"{price / (truck + train + microbus):.2f}")
print(f"{microbus / (truck + train + microbus) * 100:.2f}%")
print(f"{truck / (truck + train + microbus) * 100:.2f}%")
print(f"{train / (truck + train + microbus) * 100:.2f}%")



