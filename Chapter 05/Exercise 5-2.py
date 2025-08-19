# main function
def main():
    # Call the function and print the result for testing.
    print(repeat('Hi', 3))


# The repeat function accepts text and multiplier
# and returns a string of text repeated multiplier times.
def repeat(text, multiplier):

    # Initialize output to an empty string.
    output = ''

    # Repeat multiplier times.
    output = text * multiplier

    # Return output.
    return output


# Call the main function.
main()
