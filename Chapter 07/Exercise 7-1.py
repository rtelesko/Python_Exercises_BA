# The main function.
def main():
    # Declare local variables.
    numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
    total = 0

    # Start with an empty list.
    valid_numbers = []

    # Loop through the numbers list and append values
    # between 0 and 100 to the valid_numbers list.
    # Also add the number to the total if it is valid.
    for num in numbers:
        if num >= 0 and num <= 100:
            valid_numbers.append(num)
            total += num

    # Calculate the average.
    average = total / len(valid_numbers)
    
    # Display the results.
    print('Total of valid numbers:', total)
    print('Average of valid numbers:', \
          format(average, '.4f'))

# Call the main function.
main()
