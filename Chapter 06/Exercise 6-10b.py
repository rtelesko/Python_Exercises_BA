# Programming Exercise 6-10

# Part II

def main():
    # Local variables
    line = ''
    name = ''
    golf_score = 0
    num_players = 0

    # Open golf.txt for reading
    with open('golf.txt', 'r') as infile:
        # Read first name
        name = infile.readline()
        
        # Read until no data 
        while name != '':
            # Read score
            golf_score = int(infile.readline())

            # Strip '\n'
            name = name.rstrip('\n')

            # Display data with one line space between the data 
            # for every two players 
            print (f'Name: {name}')
            print (f'Golf Score: {golf_score}')
            
            # Read next name
            name = infile.readline()

# Call the main function.
if __name__ == '__main__':
    main()