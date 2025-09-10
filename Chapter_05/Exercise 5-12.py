# Programming Exercise 5-12

# main function
def main():
    #local variable
    distance = 0.0

    #Set up results chart
    print ('Time\tFalling Distance')
    print ('-----------------------------')
    
    # loop on time (in seconds)
    for time in range(1, 11):
        distance = falling_distance(time)
        print(f'{time}\t{distance:.2f}')

# The falling_distance function receives an object's
# falling time and returns the distance it has fallen
# in that time
def falling_distance(time):
    fallDistance = (9.8 * time * time) / 2
    return fallDistance

# Call the main function.
main()
