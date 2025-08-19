# Programming Exercise 4-2

# Declare and initialize a variable
# for the calories burned per minute.
caloriesPerMinute = 4.2

# Declare variables for the number of calories burned,
# and the number of minutes.
caloriesBurned = 0.0
minutes = 0

print ('Minutes\t\tCalories Burned')
print ('-------------------------------')

# Execute the for loop to display calories burned.
for minutes in range(10, 31, 5):
    caloriesBurned = caloriesPerMinute * minutes
    print (minutes, "\t\t", caloriesBurned) 
