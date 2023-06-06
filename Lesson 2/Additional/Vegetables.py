# Read user input
price_vegetables = float(input())
price_fruits = float(input())
kg_fruits = int(input())
kg_vegetables = int(input())

# Logic

fruits = kg_fruits * price_fruits
vegetables = kg_vegetables * price_vegetables
bgn = fruits + vegetables
print(bgn)
euro = bgn / 1.94
# Output

print(f"{euro:.2f}")
