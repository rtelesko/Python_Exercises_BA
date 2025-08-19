# The main function.
def main():
    # Get the number of words to write to the file.
    word_count = int(input('Enter number of words to write: '))

    # Open output file.
    outfile = open('words.txt', 'w')

    # Write specified number of random numbers to the file.
    for counter in range(1, word_count + 1):
        # Get a word.
        print('Word', counter, 'of', word_count, '- ', end='')
        word = input('Enter a word: ')

        # Write the word to the file.
        outfile.write(word + '\n')

    # Close the file.
    outfile.close()


# Call the main function.
main()

