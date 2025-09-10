# Programming Exercise 8-11

# The program assumes the input includes no proper nouns.

def main():
    # Set up local variables.
    result = ''
    
    # Receive user input.
    user_string = input('Enter a string: ')

    # Copy first letter in the string in its capitalized form.
    result = result + user_string[0]
    
    for i in range(1, len(user_string)):

        ch = user_string[i]

        # If the next character is in upper case set a space
        # for the new word and convert the letter to lower case.
        if ch.isupper():
            ch = ch.lower()
            result = result + ' '

        result = result + ch

    print(result)

# Call the main function.
if __name__ == '__main__':
    main()