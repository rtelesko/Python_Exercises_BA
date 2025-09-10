# Programming Exercise 7-5

def main():
    # Local variables
    test_account = ''

    try:
        # Open the file for reading
        with open('charge_accounts.txt', 'r') as input_file:
            # Read all the lines in the file into a list
            accounts = input_file.readlines()

            # Strip trailing '\n' from all elements of the list
            for i in range(len(accounts)):
                accounts[i] = accounts[i].rstrip('\n')

            # Get user input
            test_account = input('Enter the account number to be validated: ')

            # Use in operator to search for the account specified by user
            if test_account in accounts:
                print(f'Account number {test_account} is valid.')
            else:
                print(f'Account number {test_account} is not valid.')
    
    except FileNotFoundError:
        print('The file could not be found')
    except:
        print('An error occurred')

# Call the main function.
if __name__ == '__main__':
    main()