# Read user input
pages = int(input())
pages_per_hour = int(input())
days = int(input())

# Logic

hours = int(pages / pages_per_hour)
hours_per_day = int(hours / days)

# Output
# print (hours)

print(hours_per_day)
