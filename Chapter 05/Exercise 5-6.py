# Programming Exercise 5-6

# Global constants for stadium seating
CLASS_A_SEATS = 20
CLASS_B_SEATS = 15
CLASS_C_SEATS = 10

# main module
def main():
    # Local variables
    countAseats = 0
    countBseats = 0
    countCseats = 0
    incomeAseats = 0.0
    incomeBseats = 0.0
    incomeCseats = 0.0

    # Get A count
    countAseats = int(input('Enter count of A seats: '))

    # Get B count
    countBseats = int(input('Enter count of B seats: '))

    # Get C count
    countCseats = int(input('Enter count of C seats: '))

    # Calculate A income
    incomeAseats = countAseats * CLASS_A_SEATS

    # Calculate B income
    incomeBseats = countBseats * CLASS_B_SEATS

    # Calculate C income
    incomeCseats = countCseats * CLASS_C_SEATS

    # Print income
    showIncome(incomeAseats, incomeBseats, incomeCseats)

# The showIncome function accepts the income from class
# A, B, and C seats and displays the total income.
def showIncome(incomeAseats, incomeBseats, incomeCseats):
    # Local variable
    totalIncome = 0.0
    
    # Calculate total income
    totalIncome = incomeAseats + incomeBseats + incomeCseats
    
    # Show results
    print (f'Income from class A seats: $ {incomeAseats:,.2f}')
    print (f'Income from class B seats: $ {incomeBseats:,.2f}')
    print (f'Income from class C seats: $ {incomeCseats:,.2f}')
    print (f'Total income: $ {totalIncome:,.2f}')

# Call the main function.
main()
