# Programming Exercise 7-10

def main():

    # Setup variables
    team = ''
    win_count = 0

    try:
        # Open the file for reading.
        with open('WorldSeriesWinners.txt', 'r') as input_file:        
            # Read all the lines in the file into a list.
            winners = input_file.readlines()
        
        # Strip trailing newline characters.
        for i in range(len(winners)):
            winners[i] = winners[i].rstrip('\n')

        # Receive user input.
        team = input('Enter the name of a team: ')

        # Check if the team hasn't won any world series.
        if team not in winners:
            print(f'The {team} never won the world series.')

        # Find how many times the team won the world series.
        else:
            for item in winners:
                if item == team:
                    win_count += 1
            print(f'The {team} won the world series '
                  f'{win_count} times between 1903 and 2009.')

    except FileNotFoundError:
        print('The file could not be found.')
    except IOError:
        print('There was an IO error.')
    except IndexError:
        print('There was an indexing error.')
    except:
        print('An error occurred.')

# Call the main function.
if __name__ == '__main__':
    main()