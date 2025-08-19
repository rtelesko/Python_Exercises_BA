# Programming Exercise 3-12

# Named constants
RETAIL_PRICE = 99

# Variables
quantity = 0
fullPrice = 0.0
discountRate = 0.0
discountAmount = 0.0
totalAmount = 0.0

# Get number
quantity = int(input('Enter the number of packages purchased: '))

# Calculate the discount rate
if quantity > 99:
    discountRate = 0.40
elif quantity > 49:
    discountRate = 0.30
elif quantity > 19:
    discountRate = 0.20
elif quantity > 9:
    discountRate = 0.10
else:
    discountRate = 0

# Calculate the full price
fullPrice = quantity * RETAIL_PRICE

# Calculate the discount amount
discountAmount = fullPrice * discountRate

# Calculate the total amount
totalAmount = fullPrice - discountAmount

# Print results
print (f'Discount Amount: ${discountAmount:,.2f}')
print (f'Total Amount: ${totalAmount:,.2f}')
