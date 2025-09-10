# Programming Exercise 5-13

# main function
def main():
    # Local variables
    mass = 0.0
    velocity = 0.0
    KE = 0.0

    # Get mass
    mass = float(input('Enter the mass of the object in kilograms: '))

    # Get velocity
    velocity = float(input('Enter object velocity in meters per second: '))

    # Get kinetic energy
    KE = kinetic_energy(mass, velocity)

    # Show Kinetic Energy
    print (f'Kinetic Energy is: {KE:.2f} joules')

# The kinetic_energy function receives the mass and 
# velocity of an object and returns its kinetic energy 
def kinetic_energy(mass, velocity):
    # Local variable
    KE = 0.0
    
    KE = (mass * velocity * velocity) / 2
    return KE

# Call the main function.
main()


