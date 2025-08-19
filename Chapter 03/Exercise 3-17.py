# This program helps you select a restaurant.

# Initialize variables
vegetarian = False
vegan = False
glutenFree = False

# Any vegetarians?
response = input('Is anyone in your party a vegetarian? ')
if response == 'yes':
    vegetarian = True

# Any vegans?
response = input('Is anyone in your party a vegan? ')
if response == 'yes':
    vegan = True

# Anyone gluten free?
response = input('Is anyone in your party gluten free? ')
if response == 'yes':
    glutenFree = True

# Display the restaurant choices.
print('Here are your restaurant choices:')

if not vegetarian and not vegan and not glutenFree:
    print("Joe's Gourmet Butgers")

if not vegan and not glutenFree:
    print("Mama's Fine Italian")

if not vegan:
    print('Main Street Pizza')
    
print('Corner Cafe')
print("Chef's Kitchen")
