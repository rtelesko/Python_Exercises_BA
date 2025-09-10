# Named constants
LOTTERY_NUMBERS = 69
POWERBALL_NUMBERS = 26

def main():
    # Get a list of all the lottery numbers.
    lottery_list = get_numbers()
        
    # Create lists to hold each number's frequency. The lists
    # are initialized with each element set to 0.
    reg_frequency = [0] * (LOTTERY_NUMBERS + 1)
    pb_frequency = [0] * (POWERBALL_NUMBERS + 1)

    # Get the frequency of each regular number.
    for i in range(len(lottery_list[0])):
        # Get the next number in the list.
        num = lottery_list[0][i]

        # Increment that number's frequency.
        reg_frequency[num] += 1

    # Get the frequency of each PowerBall number.
    for i in range(len(lottery_list[1])):
        # Get the next number in the list.
        num = lottery_list[1][i]

        # Increment that number's frequency.
        pb_frequency[num] += 1

    # Display the frequency of each regular number.
    print('Frequencies of the regular numbers')
    print('----------------------------------')
    for i in range(1, len(reg_frequency)):
        print(f'{i} was chosen {reg_frequency[i]} times.')

    # Display the frequency of each PowerBall number.
    print('\nFrequencies of the PowerBall numbers')
    print('----------------------------------')
    for i in range(1, len(pb_frequency)):
        print(f'{i} was chosen {pb_frequency[i]} times.')

# The get_numbers function returns a 2-dimensional list with
# two elements. The first element is a list of the regular lottery
# numbers, and the 2nd element is a list of the PowerBall numbers.
def get_numbers():
    # Open the lottery number file.
    with open('pbnumbers.txt', 'r') as pblottery_file:
        # Read the file contents into a list.
        work_list = pblottery_file.readlines()

    # Strip the newline from each element.
    for i in range(len(work_list)):
        work_list[i] = work_list[i].rstrip('\n')

    # Split each element into individual numbers, and store the
    # individual regular numbers in a list named lotto_nums, and
    # the individual PowerBall numbers in a list named pb_numbers.
    lotto_nums = []
    pb_numbers = []
    for i in range(len(work_list)):
        number_set = work_list[i].split()
        for j in range(len(number_set) - 1):
            lotto_nums.append(int(number_set[j]))
        pb_numbers.append(int(number_set[len(number_set)-1]))

    pblottery = [[],[]]
    pblottery[0] = lotto_nums
    pblottery[1] = pb_numbers
    
    # Return the pblottery list.
    return pblottery

# Cal the main function.
if __name__ == '__main__':
    main()