# Declare variables for the fastest lap time,
# slowest lap time, and total lap time.
fastest = None
slowest = None
total = 0.0

# Get number of laps.
laps = int(input('Enter number of laps: '))

# Repeat for each lap.
for lap in range(1, laps + 1):

    # Get lap time.
    print('\nLap', lap, 'of', laps)
    lap_time = float(input('Enter lap time: '))

    # Check if lap is fastest so far.
    if fastest == None or lap_time < fastest:
        fastest = lap_time

    # Check if lap is slowest so far.    
    if slowest == None or lap_time > slowest:
        slowest = lap_time

    # Keep running total of lap times.
    total += lap_time

# Print fastest, slowest and average lap time.
print('\nFastest Lap Time:', fastest)
print('Slowest Lap Time:', slowest)
print('Average Lap Time:', round(total / laps, 2))




