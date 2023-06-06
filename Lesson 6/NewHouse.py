# Read user input
flowers_type = input()
flowers_count = int(input())
budget = int(input())

rose_price = 5
dahlias_price = 3.8
tulip_price = 2.8
narcissus_price = 3
gladiolus_price = 2.5

total_price = 0
# Logic

if flowers_type == 'Roses':
    total_price = rose_price *flowers_count
    if flowers_count > 80:
        total_price = rose_price * flowers_count * 0.9
elif flowers_type == 'Dahlias':
    total_price = dahlias_price * flowers_count
    if flowers_count > 90:
        total_price = flowers_count * dahlias_price * 0.85
elif flowers_type == 'Tulips':
    total_price = tulip_price * flowers_count
    if flowers_count >80:
        total_price = tulip_price * flowers_count * 0.85
elif flowers_type == 'Narcissus':
    total_price = narcissus_price * flowers_count
    if flowers_count < 120:
        total_price = narcissus_price * flowers_count * 1.15
elif flowers_type == 'Gladiolus':
    total_price = gladiolus_price * flowers_count
    if flowers_count < 80:
        total_price = flowers_count * gladiolus_price * 1.2

# Output
if total_price <= budget:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")