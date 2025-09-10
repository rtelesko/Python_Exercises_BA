# Programming Exercise 5-14

# main function
def main():
    # Local variables
    average = 0.0
    score1 = 0.0
    score2 = 0.0
    score3 = 0.0
    score4 = 0.0
    score5 = 0.0

    # Get scores
    score1 = float(input('Enter score 1: '))
    score2 = float(input('Enter score 2: '))
    score3 = float(input('Enter score 3: '))
    score4 = float(input('Enter score 4: '))
    score5 = float(input('Enter score 5: '))

    # Calculate average grade
    average = calc_average(score1, score2, score3, score4, score5)

    #Display grade and average information in tabular form
    print(f'Score\t\tNumeric Grade\tLetter Grade')
    print(f'----------------------------------------------------')
    print(f'score 1:\t{score1}\t\t{determine_grade(score1)}')
    print(f'score 2:\t{score2}\t\t{determine_grade(score2)}')
    print(f'score 3:\t{score3}\t\t{determine_grade(score3)}')
    print(f'score 4:\t{score4}\t\t{determine_grade(score4)}')
    print(f'score 5:\t{score5}\t\t{determine_grade(score5)}')
    print(f'Average score:\t{average}\t\t{determine_grade(average)}')

# The calc_average function returns average of 5 grades 
def calc_average(s1, s2, s3, s4, s5):
    return  (s1 + s2 + s3 + s4 + s5) / 5.0

# The determine_grade function receives a numeric  
# grade and returns the corresponding letter grade 
def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Call the main function.
main()


