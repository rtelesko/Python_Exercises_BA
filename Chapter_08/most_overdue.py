# Named constants
LOTTERY_NUMS = 69
MAX_NUM_OVERDUE = 10

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

# The get_last_positions function accepts a list of numbers, and the max number
# found in the list as arguments. It creates a list named last_position where
# last_position[i] contains the last subscript of number_list that contains i.
# The function returns the last_position list.
def get_last_position(number_list, max_number):
    # Create a list to hold each number's last position. The list
    # is initialized with each element set to 0.
    last_position = [0] * (max_number + 1)
    
    for i in range(len(number_list)):
        # Get the next lottery number in the list.
        num = number_list[i]

        # Store that number's position.
        last_position[num] = i

    # Return the last_position list.
    return last_position

# The position_of_lowest_value function returns the position of the
# lowest value in num_list.
def position_of_lowest_value(num_list):
    lowest = num_list[1]
    lowest_position = 1
    for i in range(2, len(num_list)):
        if num_list[i] < lowest:
            lowest = num_list[i]
            lowest_position = i

    return lowest_position

# The most_overdue function accepts pos_list, and returns another
# list in which element 0 contains the most overdue value in
# pos_list, element 1 contains the 2nd most overdue value in
# pos_list, etc.
def most_overdue(pos_list):
    # Make an empty list to hold the most overdue items.
    overdue_sorted = []
    
    # Make a copy of pos_list.
    temp_list = []
    for item in pos_list:
        temp_list.append(item)

    # Get the max value in temp_list.
    max_value = max(temp_list)

    # Determine the max number of overdue numbers to track.
    if MAX_NUM_OVERDUE < len(temp_list):
        num_overdue = MAX_NUM_OVERDUE
    else:
        num_overdue = len(temp_list)

    # Get the most overdue numbers.
    for i in range(num_overdue):
        position = position_of_lowest_value(temp_list)
        overdue_sorted.append(position)
        temp_list[position] = max_value + 1

    # Return the common_sorted list.
    return overdue_sorted

def main():
    # Get a list of all the lottery numbers.
    lotto_nums = get_all_numbers()

    # Get a list of last positions. 
    last_position_list = get_last_position(lotto_nums, LOTTERY_NUMS)
        
    # Get a list of the most overdue values.
    most_overdue_nums = most_overdue(last_position_list)

    # Determine the max number of overdue numbers to track.
    if MAX_NUM_OVERDUE < len(most_overdue_nums):
        num_overdue = MAX_NUM_OVERDUE
    else:
        num_overdue = len(most_overdue_nums)

    # Display the 10 most overdue numbers.
    print('10 Most Overdue Numbers')
    print('-----------------------')
    for i in range(num_overdue):
        print(most_overdue_nums[i])

# Call the main function.
if __name__ == '__main__':
    main()