# Programming Exercise 9-2

import random

def main():
    # Initialize dictionary
    capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
                
    # Local variables
    correct = 0
    wrong = 0
    next_question = True
    index = 0
    user_solution = ''

    # Continue until user quits the game.
    while next_question:

        # Get access to the list of state names.
        state_iterator = iter(capitals)

        # Get a random state name for the question.
        index = (random.randint(1,50) - 1)
        for i in range (index-1):
            temp = state_iterator.__next__()
        current_state = str(state_iterator.__next__())

        # Get user solution.
        user_solution = input(f'What is the capital of {current_state}? '
                              f'(or enter 0 to quit): ')
        # User wants to quit the game.
        if user_solution == '0': 
            next_question = False
            print(f'You had {correct} correct responses and '
                  f'{wrong} incorrect responses.')
        # User solution is correct.
        elif user_solution == capitals[current_state]:
            correct = correct + 1
            print('That is correct.')
        # User solution is incorrect.
        else:
            wrong = wrong + 1
            print('That is incorrect.')

# Call the main function.
if __name__ == '__main__':
    main()