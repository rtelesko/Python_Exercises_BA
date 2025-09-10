# Programming Exercise 5-4

# main module
def main():
    # Local variables
    loan = 0.0
    insurance = 0.0
    gas = 0.0
    oil = 0.0
    tires = 0.0
    maintenance = 0.0

    # Get the amount of the loan payment.
    loan = float(input('Enter the monthly loan amount: '))

    # Get the amount of insurance.
    insurance = float(input('Enter the monthly insurance amount: '))

    # Get the amount of gas.
    gas = float(input('Enter the monthly gas amount: '))

    # Get the amount of oil.
    oil = float(input('Enter the monthly oil amount: '))

    # Get the amount for tires.
    tires = float(input('Enter the monthly tires amount: '))

    # Get the amount for maintenance.
    maintenance = float(input('Enter the monthly maintenance amount: '))
        
    # Print information about the vehicle.
    showExpenses(loan, insurance, gas, oil, tires, maintenance)

# The showExpenses function accepts loan, insurance,
# gas, oil, tires, and maintenance information as
# arguments and displays the equivalent total expense
# information.
def showExpenses(loan, insure, gas, oil, tires, maintenance):
    # Local variables
    totalMonth = 0.0
    totalYear = 0.0
    totalMonth = loan + insure + gas + oil + tires + maintenance
    totalYear = totalMonth * 12

    # Print monthly and annual information.
    print (f'Total monthly expense: ${totalMonth:,.2f}')
    print (f'Total annual expense: ${totalYear:,.2f}')

# Call the main function.
main()
