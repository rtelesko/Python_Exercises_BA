# Programming Exercise 6-5

def main():
    # Declare variables
    line = ''
    total = 0.0
    number = 0.0

    # Open numbers.txt file for reading
    with open('numbers.txt', 'r') as infile:
        for line in infile:
            number = float(line)
            total += number
        
    # Display the total of the numbers in the file
    print(f'Total: {total}')

# Call the main function.
if __name__ == '__main__':
    main()