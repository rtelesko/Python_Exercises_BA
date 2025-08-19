# Programming Exercise 3-2

# Local variables
lengthA = 0.0
widthA = 0.0
areaA = 0.0
lengthB = 0.0
widthB = 0.0
areaB = 0.0

# Get length A
lengthA = float(input('Enter length A: '))

# Get width A
widthA = float(input('Enter width A: '))

# Get length B
lengthB = float(input('Enter length B: '))

# Get width B
widthB = float(input('Enter width B: '))

# Calculate area A
areaA = lengthA * widthA

# Calculate area B
areaB = lengthB * widthB

# Print area comparison
print (f'Area A: {areaA:.2f}')
print (f'Area B: {areaB:.2f}')

if  areaA > areaB:
    print ('Area A is greater than Area B.')
elif  areaA < areaB:
    print ('Area B is greater than Area A.')
else:
    print ('Area A is equal to Area B.')
