# Programming Exercise 2-12

# Named constants
COMMISSION_RATE = 0.03
NUM_SHARES = 2000
PURCHASE_PRICE = 40.0
SELLING_PRICE = 42.75

# Variables
amountPaidForStock = 0.0  # Amount paid for the stock
purchaseCommission = 0.0  # Commission paid to purchase stock
totalPaid = 0.0           # Total amount paid
stockSoldFor = 0.0        # Amount stock sold for
sellingCommission = 0.0   # Commission paid to sell stock
totalReceived = 0.0       # Total amount received
profitOrLoss = 0.0        # Amount of profit or loss

# Calculate the amount that Joe paid for the stock, not
# including the commission.
amountPaidForStock = NUM_SHARES * PURCHASE_PRICE

# Calculate the amount of commission that Joe paid his broker
# when he bought the stock.
purchaseCommission = COMMISSION_RATE * amountPaidForStock

# Calculate the total amount that Joe paid, which is the amount
# he paid for the stock plus the commission he paid his broker.
totalPaid = amountPaidForStock + purchaseCommission

# Calcualate the amount that Joe sold the stock for.
stockSoldFor = NUM_SHARES * SELLING_PRICE

# Calculate the amount of commission that Joe paid his broker
# when he sold the stock.
sellingCommission = COMMISSION_RATE * stockSoldFor

# Calculate the amount of money left over, after Joe paid
# his broker.
totalReceived = stockSoldFor - sellingCommission

# Calculate the amount of profit or loss. If this amount is a
# positive number, it is profit. If this is a negative number it
# is a loss.
profitOrLoss = totalReceived - totalPaid

# Print the required data.
print (f'Amount paid for the stock: ${amountPaidForStock:,.2f}')
print (f'Commission paid on the purchase: ${purchaseCommission:,.2f}')
print (f'Amount the stock sold for: ${stockSoldFor:,.2f}')
print (f'Commission paid on the sale: ${sellingCommission:,.2f}')
print (f'Profit (or loss if negative): ${profitOrLoss:,.2f}')
