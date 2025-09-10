# Programming Exercise 2-10

# Variables for the number of cookies,
# cups of sugar, butter, and flour.
cookies = 0.0
sugar = 0.0
butter = 0.0
flour = 0.0

# Constants for the number of cookies, cups
# of sugar, butter, and flour in the original recipe.
COOKIES_RECIPE = 48.0
SUGAR_RECIPE = 1.5
BUTTER_RECIPE = 1.0
FLOUR_RECIPE = 2.75

# Get the number of cookies.
cookies = float(input('Enter the number of cookies: '))

# Calculate the cups of sugar needed to make the cookies.
sugar = (cookies * SUGAR_RECIPE) / COOKIES_RECIPE

# Calculate the cups of butter needed to make the cookies.
butter = (cookies * BUTTER_RECIPE) / COOKIES_RECIPE

# Calculate the cups of flour needed to make the cookies.
flour = (cookies * FLOUR_RECIPE) / COOKIES_RECIPE

# Print the amount of butter, sugar, and flour needed
# to make the specified number of cookies.
print (f'To make {cookies} cookies, you will need:')
print (f'{sugar:.2f} cups of sugar')
print (f'{butter:.2f} cups of butter')
print (f'{flour:.2f} cups of flour')
