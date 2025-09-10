# The get_price function accepts a string that is assumed to be
# in the format MM-DD-YYYY:Price. It returns the Price component
# as a float.
def get_price(str):
    # Split the string at the colon.
    items = str.split(':')
    # Return the price, as a float.
    return float(items[1])

# The get_year function accepts a string that is assumed to be
# in the format MM-DD-YYYY:Price. It returns the YYYY component
# as an int.
def get_year(str):
    # Split the string at the colon.
    items = str.split(':')
    # Split the date item at the hyphens.
    date_items = items[0].split('-')
    # Return the year, as an int.
    return int(date_items[2])

# The display_highest_per_year function steps through the gas_list
# list, displaying the highest price for each year.
def display_highest_per_year(gas_list):
    current_year = get_year(gas_list[0])
    highest = get_price(gas_list[0])
    
    for e in gas_list:
        if get_year(e) == current_year:
            if get_price(e) > highest:
                highest = get_price(e)
        else:
            print(f'Highest price for {current_year}: ${highest:.2f}')
            current_year = get_year(e)
            highest = get_price(e)

    # Display the highest for the last year.
    print(f'Highest price for {current_year}: ${highest:.2f}')

# The display_lowest_per_year function steps through the gas_list
# list, displaying the lowest price for each year.
def display_lowest_per_year(gas_list):
    current_year = get_year(gas_list[0])
    lowest = get_price(gas_list[0])

    # Step through the list.
    for e in gas_list:
        if get_year(e) == current_year:
            if get_price(e) < lowest:
                lowest = get_price(e)
        else:
            print(f'Lowest price for {current_year}: ${lowest:.2f}')
            current_year = get_year(e)
            lowest = get_price(e)

    # Display the lowest for the last year.
    print(f'Lowest price for {current_year}: ${lowest:.2f}')

def main():
    # Open the file.
    with open('GasPrices.txt', 'r') as gas_file:
        # Read the file's contents into a list.
        gas_list = gas_file.readlines()

        # Display the highest prices per year.
        display_highest_per_year(gas_list)

        # Display the lowest prices per year.
        display_lowest_per_year(gas_list)

# Call the main function.
if __name__ == '__main__':
    main()