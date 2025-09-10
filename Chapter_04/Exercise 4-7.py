# Programming Exercise 4-7

# Declare variables for the number of pennies
# per day, the number of days, and the total
# number of pennies.
dayPennies = 1 
numDays = 0
total = 0.0

# Get number of days from the user.
numDays = int(input('Enter the number of days: '))

# Display table showing salary for each day.
print ('Day\tPennies')
print ('-------------------------')

for day in range(1, numDays + 1):
    print(f'{day}\t${dayPennies / 100:,.2f}')
    total += dayPennies
    dayPennies *= 2

# Display total pay.
print(f'The total salary for {numDays} '
      f'days is: ${total/100:,.2f}')
