# Programming Exercise 4-4

# Declare variables for the distance, speed, and time.
distance = 0
speed = 0.0
time = 0

# Get the speed as input from the user.
speed = float(input('Enter the speed of the vehicle in mph: '))
    
# Get time traveled and convert to integer for full hours.
time = int(float(input('Enter the number of hours traveled: ')))

# Display the distance traveled by hour.
print ('Hour\tDistance Traveled')
print ('------------------------')

for hour in range(1, time + 1):
    distance = hour * speed
    print (hour, '\t',distance)


