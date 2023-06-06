# Read user input
pen_pack = int(input())
marker_pack = int(input())
detergent = int(input())
discount = int(input()) / 100
# Logic

pens = pen_pack * 5.8
markers = marker_pack * 7.2
detergents = detergent * 1.2


bill = pens + markers + detergents
discount_bill = bill - bill * discount
# Output
print(discount_bill)
