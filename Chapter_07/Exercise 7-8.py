# Name Search

def main():
    # Create an empty list to hold the names.
    name_list = []

    # Read the contents of the file into the list.
    with open('popular_names.txt', 'r') as name_file:
        for line in name_file:
            line = line.rstrip('\n')
            name_list.append(line)
    
    # Get a name from the user.
    name = input('Enter a name: ')

    # Search for the name and display the results.
    if name in name_list:
        print('That was a popular name between 2000 and 2009.')
    else:
        print('That was not a popular name between 2000 and 2009.')

# Call the main function.
if __name__ == '__main__':
    main()
