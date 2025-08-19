# Programming Exercise 4-13

character = '*' # The character to print
size = 7        # The number of rows and columns

# Iterate over the rows.
for row in range(size):
    
    # Each row has fewer columns.
    for col in range(size, row, -1):
        print(character, end='')
        
    # Go to the next row.
    print()


