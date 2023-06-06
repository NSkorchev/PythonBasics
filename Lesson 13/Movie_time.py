# Read user input
shooting_time = int(input())
movie_scenes = int(input())
scene_time = int(input())

# Logic
total_time = movie_scenes * scene_time + 0.15 * shooting_time

if shooting_time >= total_time:
   print(f"You managed to finish the movie on time! You have \
{round(shooting_time -  total_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need \
{round(total_time - shooting_time)} minutes.")
# Output

