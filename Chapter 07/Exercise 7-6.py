import random


# The main function.
def main():
    # Get input from user.
    number_of_dice = int(input('Enter a positive integer: '))

    # Call the roll function, passing it number_of_dice.
    dice_list = roll(number_of_dice)

    # Display the result.
    print(dice_list)


# The roll function accepts a number (num) and will return
# a sorted list of num random numbers between 1 and 6.
def roll(num):
    # Start with an empty list.
    dice = []

    # Repeat num times.
    for i in range(num):
        # Append a random number between 1 and 6 to the list.
        dice.append(random.randint(1, 6))

    # Sort the list and then return it.
    dice.sort()    
    return dice


# Call the main function.
main()
