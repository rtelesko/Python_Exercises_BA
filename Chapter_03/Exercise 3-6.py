# Programming Exercise 3-6

# Get month
month = int(input('Enter the month in numeric form: '))

# Get day
day = int(input('Enter the day of the month: '))

# Get year
year = int(input('Enter the year in two digit format: '))

# Check if month input is valid
if month > 12 or month < 1:
    print('Error: invalid month input')

# Check if day input is valid
elif day > 31 or day < 1:
    print('Error: invalid day input')

# Check if year input is valid
elif year > 99 or year < 0:
    print('Error: invalid year input')

# Input is valid
else:
    # Display magic date evaluation
    print(f'The date is {month}/{day}/{year}')
    if (day * month) == year:
        print ('This is a magic date.')
    else:
        print ('This is not a magic date.')





