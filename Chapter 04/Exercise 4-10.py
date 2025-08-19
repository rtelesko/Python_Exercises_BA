# Programming Exercise 4-10

# Constants for the increase in tuition per year,
# and the starting tuition amount.
INCREASE_PER_YEAR = 0.03
STARTING_AMOUNT = 8000.0

# Declare a variable to store the tuition.
tuition = STARTING_AMOUNT

# Calculate and print amount of increase each year.
print ('Year\t Projected Tuition (per Semester)')
print ('------------------------------------------')

for year in range(5):
    tuition += (tuition * INCREASE_PER_YEAR)
    print (f'{year + 1}\t${tuition:,.2f}')
