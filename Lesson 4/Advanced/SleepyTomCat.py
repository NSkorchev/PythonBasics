# Read user input
bankholiday = int(input())

# Logic

year = 365
work_days = year - bankholiday
play_time_work = 63 * work_days
play_time_holiday = bankholiday * 127
total_play_time: int = play_time_holiday + play_time_work

# Output
if total_play_time <= 30000:
    print(f"Tom sleeps well\n{(30000 - total_play_time) // 60:.0f} hours and {(30000 - total_play_time) % 60:.0f} minutes less for play")
else:
    print(f"Tom will run away\n{(total_play_time - 30000) // 60:.0f} hours and {(total_play_time - 30000) % 60:.0f} minutes more for play")