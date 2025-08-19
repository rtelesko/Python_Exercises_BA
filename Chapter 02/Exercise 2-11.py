# Programming Exercise 2-11

# Variables for the number of lions and tigers, total number of cats,
# and the percentage of lion and tigers.
lions = 0
tigers = 0
total = 0
percent_lions = 0.0
percent_tigers = 0.0

# Get the number of lions.
lions = int(input('Enter the number of lions: '))

# Get the number of tigers.
tigers = int(input('Enter the number of tigers: '))

# Calculate the total number of cats.
total = lions + tigers

# Calculate the percentage of lions.
percent_lions = lions / total

# Calculate the percentage of tigers.
percent_tigers = tigers / total

# Print the percentage of lions.
print(f'Lions: {percent_lions:.2%}')

# Print the percentage of tigers.
print(f'Tigers: {percent_tigers:.2%}')
