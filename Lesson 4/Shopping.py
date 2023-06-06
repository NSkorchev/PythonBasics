# Read user input
Peter_budget = float(input())
GPU_count = int(input())
CPU_count = int(input())
RAM_count = int(input())
GPU_price = 250 * GPU_count
CPU_price = 0.35 *  GPU_price * CPU_count
RAM_price = 0.1 * GPU_price * RAM_count
total_price = GPU_price + CPU_price + RAM_price

if GPU_count > CPU_count:
    total_price -= total_price * 0.15

# Logic
if Peter_budget >= total_price:
    print(f"You have {Peter_budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - Peter_budget:.2f} leva more!")
# Output

