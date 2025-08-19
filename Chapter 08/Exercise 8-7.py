# Programming Exercise 8-7

def main():
    # Local variables
    num_upper = 0
    num_lower = 0
    num_space = 0
    num_digits = 0
    data = ''
    
    # Open file text.txt for reading.
    with open('text.txt', 'r') as infile:
        # Read in data from the file.
        data = infile.read()

    # Step through each character in the file.
    # Determine if the character is uppercase,
    # lowercase, a digit, or space, and keep a
    # running total of each.
    for ch in data:
        if ch.isupper():
            num_upper = num_upper + 1
        if ch.islower():
            num_lower = num_lower + 1
        if ch.isdigit():
            num_digits = num_digits + 1
        if ch.isspace():
            num_space = num_space + 1
    
    # Display the totals.
    print(f'Uppercase letters: {num_upper}')
    print(f'Lowercase letters: {num_lower}')
    print(f'Digits: {num_digits}')
    print(f'Spaces: {num_space}')

# Call the main function.
if __name__ == '__main__':
    main()