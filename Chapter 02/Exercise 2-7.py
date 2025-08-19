# Programming Exercise 2-7

# Declare variables to hold miles driven, gallons
# of fuel used, and miles-per-gallon.
miles = 0.0
gallons = 0.0
mpg = 0.0

# Get the miles driven.
miles = float(input('Enter the miles driven: '))

# Get the gallons of fuel used.
gallons = float(input('Enter the gallons of fuel used: '))

# Calculate miles-per-gallon.
mpg = miles / gallons

# Print the result.
print (f'You used {mpg:.2f} miles per gallon.')
