# The main function
def main():
    # Declare variables.
    high_score = 0
    high_scorer = ''
    counter = 0

    # Open scores.txt file for reading.
    infile = open('scores.txt', 'r')

    # Priming read.
    name = infile.readline()
      
    # Read in until no more data.
    while name != '':
        counter += 1 # Increment the counter.

        # Read the score and convert it to an integer.
        score = int(infile.readline())

        # Check for high score.
        if score > high_score:
            high_score = score
            high_scorer = name

        # Read the name of the next record.
        name = infile.readline()
        
    # Close file.
    infile.close()

    # Display the results.
    print('High Score:', high_score)
    print('Held By:', high_scorer)
    print('Number of Scores:', counter)


# Call the main function.
main()

