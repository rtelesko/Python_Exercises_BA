# Programming Exercise 5-19

import random

# main function
def main():

    # Initializing local variables
    number = 0
    play = 1

    # Continue presenting numbers for the user
    # to guess while the user wants to continue
    # playing.
    while(play > 0):
        number = random.randint(1, 100)
        play = playGuessingGame(number)

    print('Thanks for playing!')

# The playGuessingGame function receives the number that the
# user has to guess as an argument and prompts the user for
# guesses. If the user guesses incorrectly he is notified,
# and is prompted to try again. Otherwise, the user's guess
# is returned. 
def playGuessingGame(number):
    # Get the user's guess.
    userGuess = int(input('Enter a number between 1 and 100, '
                          'or 0 to quit: '))

    # As long as user doesn't want to quit
    while userGuess > 0:
        if userGuess > number:
            print('Too high, try again')
            userGuess = int(input('Enter a number between 1 '
                                  'and 100, or 0 to quit: '))
        elif userGuess < number:
            print('Too low, try again')
            userGuess = int(input('Enter a number between 1 '
                                  'and 100, or 0 to quit: '))
        else:
            print('Congratulations! You guessed the right number!')
            return userGuess  # Start the game again

    return userGuess # UserGuess is 0 and user wants to quit.

# Call the main function.
main()


