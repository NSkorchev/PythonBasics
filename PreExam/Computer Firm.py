# Read user input
n = int(input())
sales = 0
total_sales = 0
total_raiting = 0
# Logic
for i in range(n):
    sales_rating = input()
    sales = int(sales_rating[0:2])

    if sales_rating[2] == '2':
        sales = 0
    elif sales_rating[2] == '3':
        sales *= 0.5
    elif sales_rating[2] == '4':
        sales *= 0.7
    elif sales_rating[2] == '5':
        sales *= 0.85
    elif sales_rating[2] == '6':
        sales *= 1

    total_raiting += int(sales_rating[2])
    total_sales += sales

# Output
print(f'{total_sales:.2f}')
print(f'{total_raiting / n:.2f}')