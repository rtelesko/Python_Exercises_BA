# Programming Exercise 5-8

# Variable declarations
sales = 0.0
stateTax = 0.0
countyTax = 0.0
totalTax = 0.0

# Constants for the state and county tax rates
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

# Get the total sales for the month.
sales = float(input('Enter the total sales for the month: '))

# Calculate the state sales tax.
stateTax = sales * STATE_TAX_RATE

# Calculate the county sales tax.
countyTax = sales * COUNTY_TAX_RATE

# Calculate the total tax.
totalTax = stateTax + countyTax

# Print the tax information.
print(f'State Tax: ${stateTax:,.2f}')
print(f'County Tax: ${countyTax:,.2f}')
print(f'Total Tax: ${totalTax:,.2f}')



