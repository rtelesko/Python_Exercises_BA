# Programming Exercise 5-15

import random

# main function
def main():
    # Local variables
    currentNumber = 0
    oddCounter = 0
    evenCounter = 0
    totalNumbers = 100

    for counter in range(totalNumbers):

        # get random number
        currentNumber = random.randint(1, 1000)

        # Check whether number is odd or even
        if isEven(currentNumber):
            evenCounter+=1
        else:
            oddCounter+=1

    print (f'Out of {totalNumbers} random numbers, {oddCounter} '
           f'were odd, and {evenCounter} were even.')

# The isEven function returns True if number is even, False if odd. 
def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Call the main function.
main()


