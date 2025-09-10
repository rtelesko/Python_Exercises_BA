# Named constants
JAN_DAYS = 31
FEB_DAYS = 28
MARCH_DAYS = 31
APRIL_DAYS = 30
MAY_DAYS = 31
JUNE_DAYS = 30
JULY_DAYS = 31
AUG_DAYS = 31
SEPT_DAYS = 30
OCT_DAYS = 31
NOV_DAYS = 30
DEC_DAYS = 31

def main():
    # Open the file.
    with open('steps.txt', 'r') as steps_file:
        # Display the average steps for each month.
        average_steps(steps_file, 'January', JAN_DAYS)
        average_steps(steps_file, 'February', FEB_DAYS)
        average_steps(steps_file, 'March', MARCH_DAYS)
        average_steps(steps_file, 'April', APRIL_DAYS)
        average_steps(steps_file, 'May', MAY_DAYS)
        average_steps(steps_file, 'June', JUNE_DAYS)
        average_steps(steps_file, 'July', JULY_DAYS)
        average_steps(steps_file, 'August', AUG_DAYS)
        average_steps(steps_file, 'September', SEPT_DAYS)
        average_steps(steps_file, 'October', OCT_DAYS)
        average_steps(steps_file, 'November', NOV_DAYS)
        average_steps(steps_file, 'December', DEC_DAYS)

def average_steps(steps_file, month_name, days):
    sum = 0
    for count in range(days):
        sum += int(steps_file.readline())
    average = sum / days
    print(f'The average steps taken in {month_name} was {average:,.1f}')

# Call the main function.
if __name__ == '__main__':
    main()