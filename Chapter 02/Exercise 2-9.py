# Import the math module.
import math

# Get radius from user.
radius = float(input('Enter radius of circle: '))

# Calculate area and circumference of circle.
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Print the results.
print('\nArea of circle:', format(area, '.2f'))
print('Circumference of circle:', format(circumference, '.2f'))


