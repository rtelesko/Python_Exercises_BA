# The main function.
def main():
    # Receive user input.
    first_name = input ('Enter your first name: ')
    last_name = input ('Enter your last name: ')

    # Display the results.
    print('\nInitials: ', first_name[0].upper(), '.', \
          last_name[0].upper(), '.', sep='')

    print('Name in Address Book: ', first_name[0].upper(), \
          first_name[1:], ' ', last_name.upper(), sep='')

    print('Username: ', first_name[0].lower(), \
          last_name.lower(), sep='')


# Call the main function.
main()

