# Programming Exercise 6-1

def main():
    # Declare local variables
    contents = ''
    
    # Open numbers.txt file for reading
    infile = open('numbers.txt', 'r')

    # Read in data and store in content
    contents = infile.read()

    # Close file
    infile.close()

    # Print contents
    print(contents)

# Call the main function.
if __name__ == '__main__':
    main()
