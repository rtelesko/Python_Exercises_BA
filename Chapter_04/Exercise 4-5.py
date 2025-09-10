# Programming Exercise 4-5

# Declare variables to hold the total rainfall,
# monthly rainfall, average rainfall, the number
# of years, and the total number of months.
totalRainfall = 0.0
monthRainfall = 0.0
averageRainfall = 0.0
years = 0
totalMonths = 0

# Get number of years
years = int(input('Enter the number of years: '))

# Get rainfall by month
for year in range(years):
    print (f'For year {year + 1}:')
    for month in range(12):
        monthRainfall = float(input('Enter the rainfall amount for the month: '))
        # Add to total number of months
        totalMonths += 1
        # Add to total rainfall amount
        totalRainfall += monthRainfall
			
# Calculate the average rainfall
averageRainfall = totalRainfall / totalMonths

print(f'For {totalMonths} months')
print(f'Total rainfall: {totalRainfall:,.2f} inches')
print(f'Average monthly rainfall: {averageRainfall:,.2f} inches')
