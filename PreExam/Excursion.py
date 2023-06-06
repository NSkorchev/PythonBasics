# Read user input
people = int(input())
nights = int(input()) * 20
transportation_card = int(input()) * 1.60
museum_ticket = int(input()) * 6
# Logic
total = people * (nights + transportation_card + museum_ticket) * 1.25
# Output
print(f'{total:.2f}')