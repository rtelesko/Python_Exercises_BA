# The get_price function accepts a string that is assumed to be
# in the format MM-DD-YYYY:Price. It returns the Price component
# as a float.
def get_price(str):
    # Split the string at the colon.
    items = str.split(':')
    # Return the price, as a float.
    return float(items[1])

# The get_date function accepts a string that is assumed to be
# in the format MM-DD-YYYY:Price. It returns the MM-DD-YYYY
# component as a string.
def get_date(str):
    # Split the string at the colon.
    items = str.split(':')
    # Return the date, as a string.
    return str(items[0])

# The highest_element_position function returns the position of the
# element in g_list with the highest value.
def highest_element_position(g_list):
    highest = get_price(g_list[0])
    position = 0
    for i in range(1, len(g_list)):
        if get_price(g_list[i]) > highest:
            highest = get_price(g_list[i])
            position = i

    # Return the position of the highest value.
    return position

# The create_high_to_low function creates a file named
# high_to_low.txt containing the elements of gas_list
# sorted from the highest price to the lowest price.
def create_high_to_low_file(gas_list):
    # Make a copy of gas_list.
    temp_list = []
    for e in gas_list:
        temp_list.append(e)
    
    # Open a file for writing.
    outputfile = open('high_to_low.txt', 'w')

    while (len(temp_list) > 0):
        # Get the index of the element with the highest price.
        highest_index = highest_element_position(temp_list)

        # Get that element.
        highest_line = temp_list[highest_index]

        # Write that element to the file.
        outputfile.write(highest_line)

        # Delete that element from the list.
        del temp_list[highest_index]

    # Close the file.
    outputfile.close()

def main():
    # Open the file.
    with open('GasPrices.txt', 'r') as gas_file:
        # Read the file's contents into a list.
        gas_list = gas_file.readlines()

        # Create the file with the elements sorted
        # by price from highest to lowest.
        create_high_to_low_file(gas_list)

# Call the main function.
if __name__ == '__main__':
    main()