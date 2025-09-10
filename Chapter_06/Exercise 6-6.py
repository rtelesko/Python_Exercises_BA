# Programming Exercise 6-6

def main():
    # Declare variables
    total = 0.0
    number = 0.0
    counter = 0
    
    # Open numbers.txt file for reading
    with open('numbers.txt', 'r') as infile:
        for line in infile:
            counter = counter + 1
            number = float(line)
            total += number
        
    # Calculate average
    average = total / counter
    
    # Display the average of the numbers in the file
    print(f'Average: {average}')

# Call the main function.
if __name__ == '__main__':
    main()