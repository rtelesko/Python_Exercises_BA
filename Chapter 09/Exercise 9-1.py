# The main function.
def main():
    # Initialize dictionaries.
    mean_radius = {'io':1821.6, 'europa':1560.8, \
                   'ganymede':2634.1, 'callisto':2410.3}

    surface_gravity = {'io':1.796, 'europa':1.314, \
                       'ganymede':1.428, 'callisto':1.235}


    orbital_period = {'io':1.769, 'europa':3.551, \
                      'ganymede':7.154, 'callisto':16.689}



    # Get input from user.
    moon = input('Enter name of Galilean moon of Jupiter: ')

    # Convert to lowercase for reliable matching in dictionaries.
    moon = moon.lower()

    # Show error message if name does not exist.
    # Otherwise, display details of specified moon.
    if moon not in mean_radius:
        print(moon.title(), 'is an invalid moon name.')
    else:
        print('Details of', moon.title(), 'are:')
        print('Mean Radius:', mean_radius[moon], 'km')
        print('Surface Gravity:', surface_gravity[moon], 'm/s²')
        print('Orbital Period:', orbital_period[moon], 'days')


# Call the main function.
main()

