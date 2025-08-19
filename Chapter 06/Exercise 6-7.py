# Programming Exercise 6-7

import random

def main():
    # Local variables
    filename = ''
    number_of_randoms = 0
    random_number = 0

    # Get the file name as input from the user.
    filename = input('Enter the name of the file to '
                     'which results should be written: ')

    # Get the number of items to write to the file.
    number_of_randoms = int(input('Enter the number of '
                                'random numbers to be '
                                'written to the file: '))

    # Open output file.
    with open(filename, 'w') as outputFile:
        # Write specified number of random numbers to the file.
        for counter in range (number_of_randoms):

            random_number = random.randint(1, 500)
            outputFile.write(str(random_number) + '\n')

# Call the main function.
if __name__ == '__main__':
    main()