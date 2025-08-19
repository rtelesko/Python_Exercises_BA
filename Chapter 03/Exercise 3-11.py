# Programming Exercise 3-11

# Local variables
number = 0
points = 0

# Get the number of books purchased from the user.
number = int(input('Enter the number of books purchased: '))

# Determine points earned.
if number == 2:
    points = 5
elif number == 4:
    points = 15
elif number == 6:
    points = 30
elif number >= 8:
    points = 60
else: 
    points = 0

# Display the number of points earned.
print(f'You have purchased {number} books.')
print(f'This earns you {points} points.')
