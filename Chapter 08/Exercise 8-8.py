# The main function.
def main():
    # Local variables
    counter = 0
    total_length = 0
    longest_word = ''    

    # Open input file
    infile = open('words.txt', 'r')

    # Read numbers from the file while keeping count 
    # and a running total
    for word in infile:
        # Strip line break from end of word and get its length.
        word = word.rstrip('\n')
        word_length = len(word)

        # Add length to total length and increment the counter.
        total_length += word_length
        counter += 1

        # Check for longest word.
        if word_length > len(longest_word):
            longest_word = word

    # Close the file.
    infile.close()

    # Determine average length.
    average_length = total_length / counter
    
    # Display the results.
    print('Number of Words:', counter)
    print('Longest Word:', longest_word)
    print('Average Word Length:', round(average_length))


# Call the main function.
main()
