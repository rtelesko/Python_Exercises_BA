import matplotlib.pyplot as plt

# Named constant
NUM_WEEKS = 52

def main():
    # Open the expense file.
    with open('1994_Weekly_Gas_Averages.txt', 'r') as gas_file:
        # Read the file contents into a list.
        gas = gas_file.readlines()

        # Strip the newline from each element.
        for i in range(len(gas)):
            gas[i] = gas[i].rstrip('\n')

        # Create a list containing the week numbers (to use as the x coords).
        x_coords = []
        for i in range(1, NUM_WEEKS + 1):
            x_coords.append(i)

        # Build the line graph.
        plt.plot(x_coords, gas)

        # Limit the X axis to the range 1-52.
        plt.xlim(xmin=1, xmax=NUM_WEEKS)

        # Add a title.
        plt.title('1994 Weekly Gas Prices')

        # Add labels to the axes.
        plt.xlabel('Weeks (by number)')
        plt.ylabel('Average Prices')

        # Display the graph.
        plt.show()

# Call the main function.
if __name__ == '__main__':
    main()