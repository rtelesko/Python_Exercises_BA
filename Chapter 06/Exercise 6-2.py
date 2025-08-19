# Programming Exercise 6-2

def main():
    # Declare variables
    line = ''
    counter = 0
    
    # Prompt for file name
    fileName = input('Enter the name of the file: ')

    # Open the specified file for reading
    infile = open(fileName, 'r')

    # Priming read
    line = infile.readline()
    counter = 1
    
    # Read in and display first five lines
    while line != '' and counter <= 5:
	# Strip '\n'
        line = line.rstrip('\n')
        print(line)
        line = infile.readline()
        # Update counter when line is read
        counter +=1  

    # Close file
    infile.close()

# Call the main function.
if __name__ == '__main__':
    main()