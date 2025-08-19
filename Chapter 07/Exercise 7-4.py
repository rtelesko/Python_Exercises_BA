# Programming Exercise 7-4

def main():
    # List to store numbers
    number_list = []

    # Variables
    low = 0.0
    high = 0.0
    total = 0.0
    average = 0.0
    number = 0

    # Prompt for numbers 
    for i in range(20):
        number = float(input(f'Enter number {i+1} of 20: '))
        number_list.append(number)

    low = min(number_list)
    high = max(number_list)
    total = sum(number_list)
    average = total / 20.0

    print (f'Low: {low}')
    print (f'High: {high}')
    print (f'Total: {total:,.2f}')
    print (f'Average: {average:,.2f}')

# Call the main function.
if __name__ == '__main__':
    main()