# The get_price function accepts a string that is assumed to be
# in the format MM-DD-YYYY:Price. It returns the Price component
# as a float.
def get_price(str):
    # Split the string at the colon.
    items = str.split(':')
    # Return the price, as a float.
    return float(items[1])

# The get_month function accepts a string that is assumed to be
# in the format MM-DD-YYYY:Price. It returns the MM component
# as an int.
def get_month(str):
    # Split the string at the hyphens.
    items = str.split('-')
    # Return the month, as an int.
    return int(items[0])

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

# The display_monthly_averages function steps through the gas_list
# list, calculating and displaying the average price for each month.
def display_monthly_averages(gas_list):
    month_names = ['January', 'February', 'March', 'April', 'May',
                   'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    current_month = get_month(gas_list[0])
    current_year = get_year(gas_list[0])
    total = 0
    count = 0
    average = 0

    # Step through the list.
    for e in gas_list:
        if (get_month(e) == current_month) and (get_year(e) == current_year):
            total += get_price(e)
            count += 1
        else:
            average = total / count
            print(f'Average price for {month_names[current_month-1]}, {current_year}: $'
                  f'{average:,.2f}')
            current_month = get_month(e)
            current_year = get_year(e)
            total = 0
            count = 0

    # Display the average for the last month.
    print(f'Average price for {month_names[current_month-1]}, {current_year}: $'
          f'{average:,.2f}')

def main():
    # Open the file.
    with open('GasPrices.txt', 'r') as gas_file:
        # Read the file's contents into a list.
        gas_list = gas_file.readlines()

        # Display the monthly average prices.
        display_monthly_averages(gas_list)

# Call the main function.
if __name__ == '__main__':
    main()