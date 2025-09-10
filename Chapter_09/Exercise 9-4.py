# Programming Exercise 9-4

def main():
    # Get name of input file.
    input_name = input('Enter the name of the input file: ')
    
    # Open the input file and read the text.
    with open(input_name, 'r') as input_file:
        text = input_file.read()
        words = text.split()

        # Create set of unique words.
        unique_words = set(words)

        # Print the results.
        print('These are the unique words in the text:')
        for word in unique_words:
            print(word)

# Call the main function.
if __name__ == '__main__':
    main()