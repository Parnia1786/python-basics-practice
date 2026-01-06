import time

my_time = int(input("Enter the time in seconds: "))

for x in range(1, my_time+1):
    print(x)
    time.sleep(1)

print("TIME'S UP!")

