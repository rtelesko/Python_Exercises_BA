# Get the purchase amount and number of instalments.
amount = float(input('Enter the purchase amount: '))
instalments = int(input('Enter the desired number of instalments: '))

# Calculate the final purchase amount and instalment cost.
finalAmount = amount * 1.05
instalmentCost = finalAmount / instalments

# Print the results.
print('\nFinal purchase amount:', format(finalAmount, '.2f'))
print('Number of instalments:', instalments)
print('Cost per instalment:', format(instalmentCost, '.2f'))


