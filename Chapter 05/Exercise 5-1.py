# Programming Exercise 5-1

# Global constant for conversion
KILOMETERS_TO_MILES = 0.6214

# main def
def main():
    # Local variables
    mykilometers = 0.0   # Variable to hold the distance in kilometers

    # Get distance in kilometers
    mykilometers = float(input('Enter the distance in kilometers: '))
    
    # Print miles
    showMiles(mykilometers)

# The showMiles function accepts kilometers as an argument
# and prints the equivalent miles.
def showMiles(kilometers):
    #Declare local variables
    miles = 0.0
    
    miles = kilometers * KILOMETERS_TO_MILES
    print (f'The conversion of {kilometers:.2f} kilometers')
    print (f'to miles is {miles:.2f} miles.')

# Call the main function.
main()
