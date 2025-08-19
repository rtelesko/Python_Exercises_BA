# Read from console
number_one = int(input("Please enter an integer: "))
number_two = int(input("Please enter an integer: "))
number_three = int(input("Please enter an integer: "))


# Define function
def find_max(a, b, c) -> int:
    if (a >= b) and (a >= c):  # If 'a' is greater than or equal to both 'b' and 'c'
        return a
    elif (b >= a) and (b >= c):  # If 'b' is greater than or equal to both 'a' and 'c'
        return b
    else:
        return c


# Call the function
print("The maximum of numbers entered is", find_max(number_one, number_two, number_three))
