# Programming Exercise 5-11

# main module
def main():
    # Local variables
    num1 = 0
    num2 = 0

    # Get numbers
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))

    # Display result
    print (f'The maximum number is: {maximum(num1, num2)}')
 
# The maximum function returns the maximum
# of the two numbers it receives as arguments
def maximum(num1, num2):
	if num1 > num2:
	    return num1
	else:
	    return num2

# Call the main function.
main()
