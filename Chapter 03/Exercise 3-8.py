# Programming Exercise 3-8

# Global variables
HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

# Local variables
numAttending = 0    # The number of people attending
numPerPerson = 0    # The number of hot dogs and buns per person
total = 0           # The total number of hot dogs and buns needed
minDogs = 0         # The minimum number of packages of hot dogs
minBuns = 0         # The minimum number of packages of hot dog buns
dogsLeft = 0        # The number of hot dogs left over from a package
bunsLeft = 0        # The number of hot dog buns left over from a package

# Get the number of people attending the cookout from the user.
numAttending = int(input('Enter the number of people attending the cookout: '))

# Get the number of hot dogs per person from the user.
numPerPerson = int(input('Enter the number of hot dogs for each person: '))

# Calculate the total number of hot dogs and buns needed.
total = numAttending * numPerPerson

# Calculate the minimum number of packages of hot dogs needed.
minDogs = total // HOT_DOGS_PER_PACKAGE

# Determine if the number of people attending is
# large enough to require more than one package
# of hot dogs.
if minDogs > 0:
    # Calculate the number of hot dogs left over
    # from a package, if any.
    dogsLeft = total % HOT_DOGS_PER_PACKAGE
    
    # If there will be left overs, add an additional
    # package of hot dogs.
    if dogsLeft != 0:
        minDogs += 1
            
# The number of people attending is small enough to
# require only a single package of hot dogs.
else:
    # Set the minimum number of packages of hot dogs to one.
    minDogs = 1
        
# Determine the number of left over hot dogs, if any.
dogsLeft = HOT_DOGS_PER_PACKAGE * minDogs - total

# Calculate the minimum number of packages of
# hot dog buns needed.
minBuns = total // BUNS_PER_PACKAGE

# Determine if the number of people attending is
# large enough to require more than one package
# of hot dog buns.
if minBuns > 0:
    # Calculate the number of hot dog buns left over
    # from a package, if any.
    bunsLeft = total % BUNS_PER_PACKAGE
        
    # If there will be left overs, add an additional
    # package of hot dog buns.
    if bunsLeft != 0:
        minBuns += 1
            
# The number of people attending is small enough to
# require only a single package of hot dog buns.            
else:
    # Set the minimum number of packages of
    # hot dog buns to one.
    minBuns = 1

# Calculate the number of hot dog buns left over, if any.
bunsLeft = BUNS_PER_PACKAGE * minBuns - total
    
# Display the minimum packages of hot dogs needed.
print(f'Minimum packages of hot dogs needed: {minDogs}')

# Display the minimum packages of buns needed.
print(f'Minimum packages of hot dog buns needed: {minBuns}')

# Display the number of hot dogs left over.
print(f'Hot dogs left over: {dogsLeft}')

# Display the number of hot dog buns left over.
print(f'Hot dog buns left over: {bunsLeft}')
