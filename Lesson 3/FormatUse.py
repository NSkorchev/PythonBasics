import time
# Read user input
time.sleep(2)
price = float(input("Price: "))

product = 'cola'
# Logic
if price < 20:
    print('The price of {} is {} and is cheap'.format(product, price))
elif price < 10:
    print('The price of {} is {} and is cheap'.format(product, price))
else:
    print('The price of {} is {} and is expensive'.format(product, price))
# Output
