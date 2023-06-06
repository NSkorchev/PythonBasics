# Read user input
chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())
# Logic
chicken = chicken_menu * 10.35
fish = fish_menu * 12.4
vegetarian = vegetarian_menu * 8.15
desert = (chicken + fish + vegetarian) * 0.2
delivery = 2.5

total = chicken + fish + vegetarian + desert + delivery
# Output
print(total)
