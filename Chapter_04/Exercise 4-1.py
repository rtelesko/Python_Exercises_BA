# Programming Exercise 4-1

# Initialize variables for bugs and
# total number of bugs collected.
bugs = 0
total = 0

# Get number of bugs collected each day
for day in range(5):
    bugs = int(input('Enter the number of bugs collected today: '))
    total += bugs   

# Display the total number of bugs collected.
print (f'Total bugs collected: {total}')
