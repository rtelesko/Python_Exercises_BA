# Programming Exercise 8-2

def main():
    # Get a string of numbers as input from the user.
    number_string = input('Enter a sequence of digits '
                          'with nothing separating them: ')

    # Call string_total method, and store the total.
    total = string_total(number_string)

    # Display the total.
    print(f'The total of the digits in the '
          f'string you entered is {total}')


# The string_total method receives a string and returns
# the total of all the digits contained in the string.
# The method assumes that the string does not contain
# non-digit characters
def string_total(string):
    # Local variables
    total = 0
    number = 0

    # Step through each character in the string.
    for i in range(len(string)):
        # Convert the character to an integer.
        number = int(string[i])
        # Add the value to the running total.
        total += number

    # Return the total.
    return total

# Call the main function.
if __name__ == '__main__':
    main()