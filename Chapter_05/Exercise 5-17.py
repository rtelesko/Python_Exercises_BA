# Programming Exercise 5-17

# main function
def main():
    # local variable
    totalNumbers = 100
    print('number', '\t', 'is prime')
    print('------------------------')

    # For each number, print whether or not it is prime
    for number in range(1, totalNumbers + 1):

        # Show if number is prime
        if is_prime(number):
            print (number, '\t', 'prime')
        else:
            print (number, '\t', 'not prime')

# The is_prime function receives a number as an argument,
# and returns True if number is prime, False otherwise. 
def is_prime(number):
    # Local variables
    half = int(number / 2)
    status = True

    for count in range(2, half + 1):
        if number % count == 0:
            status = False
        
    return status

# Call the main function.
main()


