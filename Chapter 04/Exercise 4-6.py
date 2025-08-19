# Print table heading.
print ('Miles\tKilometers')
print ('------------------')

# Repeat for 10, 20, 30, 40, 50, 60, 70, and 80.
for miles in range(10, 81, 10):
    # Calculate the value in kilometers.
    kilometers = round(miles * 1.60934, 2)

    # Print row of data.
    print(miles, '\t', kilometers, sep='')
