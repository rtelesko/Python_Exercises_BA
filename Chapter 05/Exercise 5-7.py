# Programming Exercise 5-7

# Global constants for paint job estimator
FEET_PER_GALLON = 112
LABOR_HOURS = 8
LABOR_CHARGE = 35

# main module
def main():
    # Local variables
    pricePaint = 0.0
    feetWall = 0.0
    gallonPaint = 0
    hourLabor = 0
    costPaint = 0.0
    costLabor = 0.0

    # Get wall space
    feetWall = float(input('Enter wall space in square feet: '))

    # Get paint price
    pricePaint = float(input('Enter paint price per gallon: '))
        
    # Calculate gallons of paint
    gallonPaint = int(feetWall / FEET_PER_GALLON) + 1

    # Calculate labor hours
    hourLabor = gallonPaint * LABOR_HOURS

    # Calculate labor charge
    costLabor = hourLabor * LABOR_CHARGE

    # Calculate paint cost
    costPaint = gallonPaint * pricePaint

    # Print cost estimate
    showCostEstimate(gallonPaint, hourLabor, costPaint, costLabor)

# The showCostEstimate function accepts gallonPaint, hourLabor,
# costPaint, costLabor as arguments and displays the corresponding
# data.
def showCostEstimate(gallonPaint, hourLabor, costPaint, costLabor):
    # Local variable
    totalCost = 0.0

    # Calculate total cost
    totalCost = costPaint + costLabor

    # Display results
    print (f'Gallons of paint: {gallonPaint}')
    print (f'Hours of labor: {hourLabor}')
    print (f'Paint charges: ${costPaint:,.2f}')
    print (f'Labor charges: ${costLabor:,.2f}')
    print (f'Total cost: ${totalCost:,.2f}')

# Call the main function.
main()
