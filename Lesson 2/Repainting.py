# Read user input
nylon_sq = int(input())
paint_l = int(input())
paint_thinner_l = int(input())
man_hour = int(input())
# Logic
nylon = (nylon_sq + 2) * 1.5
paint = (paint_l * 0.1 + paint_l) * 14.5 + 0.4
paint_thinner = paint_thinner_l * 5
workforce = man_hour * (nylon + paint + paint_thinner) * 0.3

total = workforce + nylon + paint + paint_thinner
# Output
# print(nylon)
# print(paint)
# print(paint_thinner)
# print(man_hour)
# print(workforce)
print(total)
