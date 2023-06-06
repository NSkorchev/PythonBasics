# Read user input
first_time = int(input())
second_time = int(input())
third_time = int(input())
# Logic

total_time = first_time + second_time + third_time
minutes = total_time // 60
seconds = total_time % 60

# seconds = "0" + str(seconds) if seconds < 10 else seconds

if seconds < 10:
    # seconds = "0" + str(seconds)
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
# Output
    # print(f"{minutes}:{seconds}")