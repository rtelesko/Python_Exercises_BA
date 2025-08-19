# Programming Exercise 3-9

# Local variables
pocketNum = 0
outputStr = ''

# Get the pocket number from the user.
pocketNum = int(input('Enter a pocket number from 0 to 36: '))

# Determine if the pocket number is valid.
if pocketNum < 0 or pocketNum > 36:
    outputStr = 'Error: Invalid input'
    
# Determine the color of the pocket number.
else:
    # For pockets 1 through 10, the odd-numbered pockets
    # are red and the even-numbered pockets are black.    
    if pocketNum >= 1 and pocketNum <= 10:
        if pocketNum % 2:   
            outputStr = 'Black' # Even
        else:
            outputStr = 'Red'   # Odd
            
    # For pockets 11 through 18, the odd-numbered pockets
    # are black and the even-numbered pockets are red.              
    elif pocketNum >= 11 and pocketNum <= 18:
        if pocketNum % 2:
            outputStr = 'Red'   # Even
        else:
            outputStr = 'Black' # Odd
            
    # For pockets 19 through 28, the odd-numbered pockets
    # are red and the even-numbered pockets are black.              
    elif pocketNum >= 19 and pocketNum <= 28:
        if pocketNum % 2:
            outputStr = 'Black' # Even
        else:
            outputStr = 'Red'   # Odd
            
    # For pockets 29 through 36, the odd-numbered pockets
    # are black and the even-numbered pockets are red.              
    elif pocketNum >= 29 and pocketNum <= 36:
        if pocketNum % 2:
            outputStr = 'Red'   # Even
        else:
            outputStr = 'Black' # Odd
            
    # Pocket 0 is green.
    else:
       outputStr = 'Green'      # Zero

# Display the output.
print(outputStr)
