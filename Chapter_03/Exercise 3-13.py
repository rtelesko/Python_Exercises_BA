# Programming Exercise 3-13

# Local variables
weight = 0.0
shippingCost = 0.0

# Get package weight from the user.
weight = float(input('Enter the weight of the package: '))

# Calculate the shipping charge.
if weight > 10:
    shippingCost = 4.75
elif weight > 6:
    shippingCost = 4.00
elif weight > 2:
    shippingCost = 3.00
else:
    shippingCost = 1.50

# Display the shipping charge.
print (f'Shipping charge: ${shippingCost:,.2f}')
