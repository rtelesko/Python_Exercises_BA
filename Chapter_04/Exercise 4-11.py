# Declare constants.
DESIRABLE_SLEEP = 8
DAYS = 7

# Declare accumulator variable for total sleep.
total_sleep = 0

# Repeat DAYS number of times.
for day in range(1, DAYS + 1):
    # Get amount of sleep for current day.
    print('Day', day, 'of', DAYS)
    sleep = int(input('Enter hours of sleep obtained: '))

    # Add it to total sleep accumulator.
    total_sleep += sleep

# Calculate the user's sleep debt.
sleep_debt = (DESIRABLE_SLEEP * DAYS) - total_sleep
    
# Display result.
if sleep_debt > 0:
    print('Total Sleep Debt:', sleep_debt, 'hour(s).')
else:
    print('You do not have a sleep debt...')
    print('I wish I could say the same!')
