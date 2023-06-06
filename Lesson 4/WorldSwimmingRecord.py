# Read user input
record_sec = float(input())
distance_m = float(input())
time_m_s = float(input())

# Logic
slowness = distance_m // 15 * 12.5

time = distance_m * time_m_s + slowness

if time < record_sec:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    print(f"No, he failed! He was {time - record_sec:.2f} seconds slower.")

# Output
