# Programming Exercise 3-14

# Local variables
days = 0
hours = 0
minutes = 0
seconds = 0 
dayRemainder = 0
hourRemainder = 0
minuteRemainder = 0

# Get the number of seconds from the user.
seconds = int(input('Enter the number of seconds: '))

# Calculate the number of days.
if seconds >= 86400:
    days = seconds // 86400
    dayRemainder = seconds % 86400
    
# Calculate the hours.
if seconds >= 3600:
    hours = seconds // 3600
    hourRemainder = seconds % 3600
        
# Calculate the minutes.
if seconds >= 60:
    minutes = seconds // 60
    minuteRemainder = seconds % 60
        
# Display days, hours, minutes, seconds.
if minutes == 0:
    print('The number of seconds is less than one minute.')
else:
    print(f'{seconds} seconds are equal to:')
    print(f'{minutes} full minute(s) and {minuteRemainder} seconds.')
    if hours!=0:
        print (f'{hours} full hour(s) and {hourRemainder} seconds.')
    if days!=0:
        print (f'{days} full day(s) and {dayRemainder} seconds.')
