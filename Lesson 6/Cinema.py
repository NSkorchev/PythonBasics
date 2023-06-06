# Read user input
movie_type = input()
rows = int(input())
columns = int(input())

# Logic
income = 0
cinema_capacity = rows * columns

if movie_type == 'Premiere':
    income = cinema_capacity * 12
elif movie_type == 'Normal':
    income = cinema_capacity * 7.5
else:
    income = cinema_capacity * 5

print(f'{income:.2f} leva')
# Output
