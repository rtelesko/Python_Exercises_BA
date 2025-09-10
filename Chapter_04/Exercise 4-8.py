# Programming Exercise 4-8

# Declare variables for the number, and the
# total.
number = 1.0    # Initialize for while loop
total = 0.0

# Continue adding numbers while they are positive.
while number > 0:
    number = float(input('Enter a positive number (negative to quit): '))

    # Check that number is positive so as
    # not to change value of the total.
    if number > 0:
        total = total + number

# Display total.
print (f'Total = {total:.2f}') 
