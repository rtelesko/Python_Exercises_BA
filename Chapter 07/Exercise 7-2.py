# Programming Exercise 7-2

import random

def main():
    # Initialize list of numbers.
    number_list = [0, 0, 0, 0, 0, 0, 0]

    # Assign random numbers to list.
    for i in range(7):
        number_list[i] = random.randint(0, 9)

    # Display numbers in a single line.
    for i in range(7):
        print (number_list[i], end='')
        
        # Separate current number from next number.
        if i < 6:
            print(', ', end='')

# Call the main function.
if __name__ == '__main__':
    main()