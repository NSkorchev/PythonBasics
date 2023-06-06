# Read user input
hour_exam = int(input())
minute_exam = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

# Logic

if hour_exam > 23:
    hour_exam %= 24
if minute_exam > 59:
    hour_exam += minute_exam // 60
    minute_exam %= 60
if arrival_hour > 23:
    arrival_hour %= 24
if arrival_minute > 59:
    arrival_hour += arrival_minute // 60
    arrival_minute %= 60

exam_time_minutes = hour_exam * 60 + minute_exam
arrival_time_minute = arrival_hour * 60 + arrival_minute
time_diff = exam_time_minutes - arrival_time_minute

if time_diff > 30:
    print("Early")
elif time_diff < 0:
    print("Late")
else:
    print("On time")

hours = 0
minutes = abs(time_diff)

if minutes >= 60:
    hours = minutes // 60
    minutes %= 60

result = ""

if hours > 0:
    result += str(hours) + ":" + ("0" + str(minutes) if minutes < 10 else str(minutes)) + " hours"
else:
    result += str(minutes) + " minutes"

if time_diff > 0:
    result += " before the start"
else:
    result += " after the start"

print(result)

# Output
