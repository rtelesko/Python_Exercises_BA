# Programming Exercise 5-5

# Global constants for property tax
ASSESS_PERCENT = 0.6
PROPERTY_TAX_PERCENT = 0.0072

# main function
def main():
    # Local variables
    actualValue = 0.0
    assessValue = 0.0
    propertyTax = 0.0

    # Get the actual value.
    actualValue = float(input('Enter the actual value: '))

    # Calculate the assessed value.
    assessValue = actualValue * ASSESS_PERCENT

    # Calculate the property tax.
    propertyTax = assessValue * PROPERTY_TAX_PERCENT

    # Print information about property tax.
    showPropertyTax(assessValue, propertyTax)
    
# The showPropertyTax function accepts the assessment
# value and the property tax value as arguments and
# displays the property tax information.
def showPropertyTax (assessValue, propertyTax):
    print (f'Assessed value: ${assessValue:,.2f}')
    print (f'Property tax: ${propertyTax:,.2f}')

# Call the main function.
main()
