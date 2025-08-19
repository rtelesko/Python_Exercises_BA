# Programming Exercise 5-3

# Global constant for the percent of replacement cost
REPLACE_PERCENT = 0.8

# main def
def main():
    # Local variables
    replace= 0.0
    minInsure = 0.0

    # Get the replacement cost.
    replace = float(input('Enter the replacement amount: '))

    # Calculate the insurance amount
    minInsure = replace * REPLACE_PERCENT

    # Print information about the insurance.
    showInsure(replace, minInsure)
      
# The showInsure function accepts the replace value 
# and the minimum recommended insurance as arguments
# and displays the transaction information.
def showInsure (replace, minInsure):
    print (f'Replacement cost: ${replace:,.2f}')
    print (f'Percent insured: {REPLACE_PERCENT:,.2%}') 
    print (f'Minimum insurance: ${minInsure:,.2f}')

# Call the main function.
main()
