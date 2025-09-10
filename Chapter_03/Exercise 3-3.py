# Get the number for the month.
month = int(input('Enter a number (1-12) for the month: '))

# Determine the quarter of the year and display it.
if month >= 1 and month <= 3:
    print('First Quarter')
elif month >= 4 and month <= 6:
    print('Second Quarter')
elif month >= 7 and month <= 9:
    print('Third Quarter')
elif month >= 10 and month <= 12:
    print('Fourth Quarter')
else:
    print('Error: Please enter a number between 1 and 12.')


