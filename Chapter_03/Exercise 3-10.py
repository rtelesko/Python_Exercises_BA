# Programming Exercise 3-10

# Global variables
PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

# Local variables
numPennies = 0
numNickels = 0
numDimes = 0
numQuarters = 0
totalCentValue = 0.0
totalDollars = 0.0

# Get number of pennies, nickels, dimes, and
# quarters from the user.
numPennies = int(input('Enter the number of pennies: '))
numNickels = int(input('Enter the number of nickels: '))
numDimes = int(input('Enter the number of dimes: '))
numQuarters = int(input('Enter the number of quarters: '))

# Sum the pennies, nickels, dimes and quarters
# to obtain total cent value.
totalCentValue = (numPennies * PENNY_VALUE) + \
                 (numNickels * NICKEL_VALUE)+ \
                 (numDimes * DIME_VALUE) + \
                 (numQuarters * QUARTER_VALUE)

# Calculate the total value in dollars
totalDollars = totalCentValue / PENNIES_IN_DOLLAR

# Determine whether user won the game:
if totalDollars > 1.0:
    # The amount was more than one dollar.
    print('Sorry, the amount you entered was more than one dollar.')
elif totalDollars < 1.0:
    # The amount was less than one dollar.
    print('Sorry, the amount you entered was less than one dollar.')
else:
    # The amount was exactly one dollar.
    print('Congratulations!')
    print('The amount you entered was exactly one dollar!')
    print('You win the game!')

