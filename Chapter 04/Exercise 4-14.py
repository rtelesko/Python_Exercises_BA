# Programming Exercise 4-14

character = '#' # The symbol to print
numRows = 7     # The number of rows
space = ' '     # The space character

# Iterate over the rows.
for row in range(numRows):
    		
    # Each row includes 2 more columns
    # than the row number.
    for col in range(row + 2):
        
        # Print the symbol in the first
        # and last column.
        if col == 0 or col == row + 1:
            print(character, end='')
            
        # Add spaces between symbols.
        else:  
            print (space, end='')

    # Go to the next row.
    print()




