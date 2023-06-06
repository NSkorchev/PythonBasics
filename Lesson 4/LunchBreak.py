import math
# Read user input
TV_serie = input()
ep_duration = int(input())
break_duration = int(input())

# Logic

lunch_time = break_duration / 8
rest_time = break_duration / 4

time_left = break_duration - lunch_time - rest_time

if time_left >= ep_duration:
    print(f"You have enough time to watch {TV_serie} \
and left with {math.ceil(time_left - ep_duration)} minutes free time.")
else:
   print(f"You don't have enough time to watch {TV_serie}, you need {math.ceil(ep_duration - time_left)} more minutes.")
# Output
