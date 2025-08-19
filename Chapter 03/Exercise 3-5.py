# Programming Exercise 3-5

# Global constants
MASS_MULTIPLIER = 9.8
TOO_HEAVY = 500.0
TOO_LIGHT = 100.0

# Local variables   
weight = 0.0
mass = 0.0

# Get mass
mass = float(input("Enter the object's mass in kilograms: "))

# Calculate weight 
weight = mass * MASS_MULTIPLIER

# Display weight evaluation
print (f'Object Weight: {weight:.2f}')

if weight > TOO_HEAVY:
    print (f'The object is too heavy. It weighs more than '
           f'{TOO_HEAVY} Newtons.')
elif  weight < TOO_LIGHT:
    print (f'The object is too light. It weighs less than '
           f'{TOO_LIGHT} Newtons.')
