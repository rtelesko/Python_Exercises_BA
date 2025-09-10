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

# The lowest_element_position function returns the position of the
# element in g_list with the lowest value.
def lowest_element_position(g_list):
    lowest = get_price(g_list[0])
    position = 0
    for i in range(1, len(g_list)):
        if get_price(g_list[i]) < lowest:
            lowest = get_price(g_list[i])
            position = i

    # Return the position of the lowest value.
    return position

# The create_low_to_high_file function creates a file named
# low_to_high.txt containing the elements of gas_list
# sorted from the lowest price to the highest price.
def create_low_to_high_file(gas_list):
    # Make a copy of gas_list.
    temp_list = []
    for e in gas_list:
        temp_list.append(e)
    
    # Open a file for writing.
    outputfile = open('low_to_high.txt', 'w')

    while (len(temp_list) > 0):
        # Get the index of the element with the lowest price.
        lowest_index = lowest_element_position(temp_list)

        # Get that element.
        lowest_line = temp_list[lowest_index]

        # Write that element to the file.
        outputfile.write(lowest_line)

        # Delete that element from the list.
        del temp_list[lowest_index]

    # Close the file.
    outputfile.close()

def main():
    # Open the file.
    with open('GasPrices.txt', 'r') as gas_file:
        # Read the file's contents into a list.
        gas_list = gas_file.readlines()

        # Create the file with the elements sorted
        # by price from lowest to highest.
        create_low_to_high_file(gas_list)

# Call the main function.
if __name__ == '__main__':
    main()