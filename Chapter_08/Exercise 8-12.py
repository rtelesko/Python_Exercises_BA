# Programming Exercise 8-12

def main():
    # Set up local variables.
    result = ''
    current_word = ''
    ENDING = 'AY'
    
    # Receive user input.
    user_string = input('Enter a string: ')

    # Divide the input into individual words.
    words = user_string.split()

    # Loop that changes each word.
    for i in range(len(words)):

        item = words[i].upper()

        # For one letter words, just add ending.
        if len(item) == 1:
            current_word = item + ENDING

        # For words with more than one letter, 
        # Change the order and add ending.
        else:
            current_word = item[1:] + item[0] + ENDING

        # Add adapted word to the result.
        result = result + current_word

        # If more words to be added, add a space to the result.
        if i < len(words) + 1:
            result = result + ' '

    # Display the result.
    print(result)

# Call the main function.
if __name__ == '__main__':
    main()