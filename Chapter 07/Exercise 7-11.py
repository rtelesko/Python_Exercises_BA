# Programming Exercise 7-11

# Global constants
ROWS = 3    # The number of rows
COLS = 3    # The number of columns
MIN = 1     # The value of the smallest number
MAX = 9     # The value of the largest number

def main():
    # Create a two-dimensional list.
    test_list = [ [4, 9, 2],
                  [3, 5, 7],
                  [8, 1, 6] ]

    # Display the list in row and column format.
    display_square_list(test_list)
    
    # Determine if the list is a Lo Shu magic square.
    if is_magic_square(test_list):
        print('This is a Lo Shu magic square.')
    else:
        print('This is not a Lo Shu magic square.')

# The display_square_list function accepts a two-dimensional
# list as an argument, and displays the list's values in row
# and column format.
def display_square_list(value_list):
    for r in range(ROWS):
        for c in range(COLS):
            print(value_list[r][c], end=' ')
        print()

# The is_magic_square function accepts a two-dimensional
# list as an argument, and returns True if the list meets
# all the requirements of a magic square. Otherwise it
# returns False.
def is_magic_square(value_list):
    # Set status to False, initially.
    status = False
    
    # Call functions and store their return values.
    is_in_range = check_range(value_list)
    is_unique = check_unique(value_list)
    is_equal_rows = check_row_sum(value_list)
    is_equal_cols = check_col_sum(value_list)
    is_equal_diag = check_diag_sum(value_list)

    # Determine if the list meets all the requirements.
    if is_in_range and \
       is_unique and \
       is_equal_rows and \
       is_equal_cols and \
       is_equal_diag:
        
        # If it does, set status to True.
        status = True

    # Return the status.
    return status

# The check_range function accepts a two-dimensional
# list as an argument, and returns True if the values
# in the list are within the specified range. Otherwise,
# it returns False.
def check_range(value_list):
    # Initialize status to True.
    status = True

    # Step through all the values in the list.
    for r in range(ROWS):
        for c in range(COLS):
            # Determine if any of the values
            # are out of range.
            if value_list[r][c] < MIN or value_list[r][c] > MAX:
                # If so, set status to False.
                status = False
                
    # Return the status.
    return status

# The check_unique function accepts a two-dimensional
# list as an argument, and returns True if the values
# in the list are unique. Otherwise, it returns False.
def check_unique(value_list):
    # Initialize status to True.
    status = True
    # Initialize the search value.
    search_value = MIN
    # Initialize the counter to zero.
    count = 0

    # Perform the search while the maximum value
    # has not been reached, and the values are
    # unique.
    while search_value <= MAX and status == True:
        # Step through all the values in the list.
        for r in range(ROWS):
            for c in range(COLS):
                # Determine if the current value equals
                # the search value.
                if value_list[r][c] == search_value:
                    # If so, increment the counter.
                    count += 1
                # Determine if the counter variable is
                # Greater than one.
                if count > 1:
                    # If so, the value is not unique.
                    # Set status to False.
                    status = False
        # Increment the search value.
        search_value += 1
        # Reset the counter variable.
        count = 0
        
    # Return the status.
    return status

# The check_row_sum function accepts a two-dimensional
# list as an argument, and returns True if the sum of
# the values in each of the list's rows are equal.
# Otherwise, it returns False.
def check_row_sum(value_list):
    # Initialize status to True.
    status = True

    # Calculate the sum of the values in the first row.
    sum_row_0 = value_list[0][0] + \
                value_list[0][1] + \
                value_list[0][2]

    # Calculate the sum of the values in the second row.
    sum_row_1 = value_list[1][0] + \
                value_list[1][1] + \
                value_list[1][2]

    # Calculate the sum of the values in the third row.
    sum_row_2 = value_list[2][0] + \
                value_list[2][1] + \
                value_list[2][2]

    # Determine if the sum of any of the rows is not equal.
    if (sum_row_0 != sum_row_1) or \
       (sum_row_0 != sum_row_2) or \
       (sum_row_1 != sum_row_2):
        # If so, set the status to False
        status = False

    # Return the status.
    return status

# The check_col_sum function accepts a two-dimensional
# list as an argument, and returns True if the sum of
# the values in each of the list's columns are equal.
# Otherwise, it returns False.
def check_col_sum(value_list):
    # Initialize status to True.
    status = True

    # Calculate the sum of the values in the first column.
    sum_col_0 = value_list[0][0] + \
                value_list[1][0] + \
                value_list[2][0]

    # Calculate the sum of the values in the second column.
    sum_col_1 = value_list[0][1] + \
                value_list[1][1] + \
                value_list[2][1]

    # Calculate the sum of the values in the third column.
    sum_col_2 = value_list[0][2] + \
                value_list[1][2] + \
                value_list[2][2]

    # Determine if the sum of any of the columns
    # is not equal.
    if (sum_col_0 != sum_col_1) or \
       (sum_col_0 != sum_col_2) or \
       (sum_col_1 != sum_col_2):
        # If so, set the status to False
        status = False

    # Return the status.
    return status

# The check_diag_sum function accepts a two-dimensional
# list as an argument, and returns True if the sum of
# the values in each of the list's diagonals are equal.
# Otherwise, it returns False.
def check_diag_sum(value_list):
    # Initialize status to True.
    status = True

    # Calculate the sum of the values in the first diagonal.
    sum_diag_0 = value_list[0][0] + \
                value_list[1][1] + \
                value_list[2][2]

    # Calculate the sum of the values in the second diagonal.
    sum_diag_1 = value_list[2][0] + \
                value_list[1][1] + \
                value_list[0][2]

    # Determine if the sum of any of the columns
    # is not equal.
    if sum_diag_0 != sum_diag_1:
        status = False

    # Return the status.
    return status

# Call the main function.
if __name__ == '__main__':
    main()