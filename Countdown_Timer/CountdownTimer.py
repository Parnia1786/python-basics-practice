# Countdown Timer

import time

total_seconds = int(input("Enter the time in seconds: "))

for remaining_seconds in range(total_seconds, 0, -1):
    secs = remaining_seconds % 60
    mins = (remaining_seconds // 60) % 60
    hours = remaining_seconds // 3600
    print(f"{hours:02}:{mins:02}:{secs:02}")
    time.sleep(1)

print("TIME'S UP!")
