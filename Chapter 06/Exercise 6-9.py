# Programming Exercise 6-9

def main():
    # Declare local variables
    total = 0.0
    number = 0.0
    counter = 0
    
    try:
        # Open numbers.txt file for reading
        with open('numbers.txt', 'r') as infile:
            for line in infile:
                counter = counter + 1
                number = float(line)
                total += number
        
        # Calculate average
        average = total / counter
    
        # Display the average of the numbers in the file
        print (f'Average: {average}')

    except IOError:
        print('An error occurred while trying to read the file.')
    except ValueError:
        print('Non-numeric data found in the file')
    except: 
        print('An error occurred')

# Call the main function.
if __name__ == '__main__':
    main()