# The main function.
def main():
    try:
        # Get the file name.
        file_name = input('Enter the name of the file: ')
        
        # Open the specified file for reading.
        infile = open(file_name, 'r')

        # Read all data from the file into a list of strings.
        data = infile.readlines()
            
        # Close the file.
        infile.close()

        # Display number of lines in program.
        print('The file contains', len(data), 'line(s).')

        # Get the line number
        line_number = int(input('Enter the line number: '))

        # Display the line.
        line = data[line_number - 1] # Subtract 1 to match index.
        print('Line', line_number, 'is:\n', line)

    # Handle exceptions.
    except IOError:
        print('An error occurred while trying to read the file.')

    except ValueError:
        print('Invalid input: Enter an integer.')

    except IndexError:
        print('Invalid line number.')


# Call the main function.
main()

