# Programming Exercise 5-9

# main function
def main():
    
    # Local variables
    feet = 0.0
    inches = 0.0

    # Get the number of feet from the user.
    feet = float(input('Enter the number of feet: '))

    # Display the corresponding number of inches.
    inches = feet_to_inches(feet)
    print (f'{feet} feet = {inches} inches')
    
# The feet_to_inches function receives the number of
# feet and returns the number of inches in that many
# feet.
def feet_to_inches(feet):
    return 12 * feet

# Call the main function.
main()
