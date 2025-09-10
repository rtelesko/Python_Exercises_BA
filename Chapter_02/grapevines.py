# This program calculates the number of grapevines that
# can be planted in a vineyard row.

r = float(input('Enter the length of the row, in feet: '))
e = float(input('Enter the aount of space, in feet, used by an end-post assembly: '))
s = float(input('Enter the distance, in feet, between each vine: '))

# Calculate the number of vines.
v = (r - 2 * e) / s

# Display the results.
print(f'You have enough space for {v:.1f} vines.')
