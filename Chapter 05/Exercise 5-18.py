# main function
def main():

    # Get user input for amount, interest rate and months.
    amount = float(input('Enter the loan amount: '))
    
    rate = float(input('Enter the monthly interest ' \
                       'rate as a percentage: '))
    
    months = int(input('Enter the number of months: '))

    # Use function to determine monthly payment amount.
    payment = calculate_payment(amount, rate, months)

    # Display the results.
    print('\nLoan Amount: $', format(amount, ',.2f'), sep='')
    print('Monthly Interest: ', format(rate, '.2f'), '%', sep='')
    print('Payment Months:', months)
    print('\nMonthly Payment Amount: $', format(payment, ',.2f'), sep='')


# The calculate_payment function receives the loan amount, the 
# interest rate percentage, and the number of months in which to pay
# off the loan, and returns the necessary monthly payment amount. 
def calculate_payment(A, R, M):
    # Convert interest percentage to a decimal.
    dR = R / 100

    # Calculate and return payment amount.
    return (dR * A) / (1 - (1 + dR) ** -M)


# Call the main function.
main()


