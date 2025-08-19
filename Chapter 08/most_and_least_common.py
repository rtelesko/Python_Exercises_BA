# Named constants
LOTTERY_NUMBERS = 69

# The get_all_numbers function returns a list containing the
# lottery numbers in pbnumbers.txt. The numbers appear in the
# order that they were read from the file.
def get_all_numbers():
    # Open the lottery number file.
    with open('pbnumbers.txt', 'r') as pblottery_file:
        # Read the file contents into a list.
        pblottery = pblottery_file.readlines()

    # Strip the newline from each element.
    for i in range(len(pblottery)):
        pblottery[i] = pblottery[i].rstrip('\n')

    # Split each element into individual numbers, and
    # store the individual numbers in a list named lotto_nums.
    lotto_nums = []
    for i in range(len(pblottery)):
        number_set = pblottery[i].split()
        for j in range(len(number_set)):
            lotto_nums.append(int(number_set[j]))

    # Return the lotto_nums list.
    return lotto_nums

# The get_frequency function accepts a list of numbers and determines
# the freqeuncy of each item in the list. The max_value parameter
# specifies the max value that is stored in the list.
def get_frequency(number_list, max_value):
    # Create a list to hold each number's frequency. The list
    # is initialized with each element set to 0.
    frequency = [0] * (max_value + 1)
    for i in range(len(number_list)):
        # Get the next lottery number in the list.
        num = number_list[i]

        # Increment that number's frequency.
        frequency[num] += 1

    # Return the frequency list.
    return frequency

# The position_of_highest_value function returns the position of the
# highest value in num_list.
def position_of_highest_value(num_list):
    highest = 0
    highest_position = 0
    for i in range(len(num_list)):
        if num_list[i] > highest:
            highest = num_list[i]
            highest_position = i

    return highest_position

# The most_common function accepts freq_list, and returns another
# list in which element 0 contains the position of the highest value in
# freq_list, element 1 contains the position of the 2nd highest value in
# freq_list, etc.
def most_common(freq_list):
    # Make an empty list to hold the positions of the most common items.
    common_sorted = []
    
    # Make a copy of freq_list.
    temp_list = []
    for item in freq_list:
        temp_list.append(item)

    for i in range(len(temp_list)):
        position = position_of_highest_value(temp_list)
        common_sorted.append(position)
        temp_list[position] = -1

    # Return the common_sorted list.
    return common_sorted

def main():
    # Get a list of all the lottery numbers.
    lotto_nums = get_all_numbers()
        
    # Get each number's frequency.
    frequency = get_frequency(lotto_nums, LOTTERY_NUMBERS)

    # Get a list of the most common values.
    sorted_by_most_common = most_common(frequency)

    # Display the 10 most common numbers.
    print('10 Most Common Numbers (Highest to Lowest)')
    print ('-----------------------------------------')
    for i in range(10):
        print(sorted_by_most_common[i])

    # Display the 10 least common numbers.
    sorted_by_most_common.reverse()
    print('\n10 Least Common Numbers (Lowest to Highest)')
    print ('-----------------------------------------')
    for i in range(1, 11):
        print(sorted_by_most_common[i])
    
# Call the main function.
if __name__ == '__main__':
    main()