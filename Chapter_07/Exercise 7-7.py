# Programming Exercise 7-7

# The program assumes that the student's solutions are listed such 
# that each line includes the student's answer to the question, 
# without the question number preceding the answer. The student's 
# answers are assumed to be in the order of the questions.

def main():
    # Setup variables
    solution = ['A', 'C', 'A', 'A', 'D',
                'B', 'C', 'A', 'C', 'B',
                'A', 'D', 'C', 'A', 'D',
                'C', 'B', 'B', 'D', 'A']
    correct_count = 0
    incorrect_count = 0
    incorrect_questions = []
    counter = 0
    
    try:
        # Open the file for reading.
        with open('student_answers.txt', 'r') as input_file:
            # Read all the lines in the file into a list.
            student_solutions = input_file.readlines()
            
        # Strip trailing '\n' from all elements of the list.
        for i in range(len(student_solutions)):
            student_solutions[i] = student_solutions[i].rstrip('\n')

        # Compare student solution to correct solution and update
        # appropriate counters.
        for i in range(len(student_solutions)):
            if student_solutions[i] == solution[i]:
                correct_count += 1
            else:
                incorrect_count += 1
                incorrect_questions.append(str(i + 1))

        # Determine if student passed and display result.
        if correct_count >= 15:
            print('Congratulations!! You passed the exam.')
        else:
            print('Sorry, you did not pass the exam.')

        # Display exam details.
        print(f'Number of questions you answered correctly: {correct_count}')
        print(f'Number of questions you answered incorrectly: {incorrect_count}')
        
        # Determine if the student got any questions wrong.
        if incorrect_count > 0:
            # Display the numbers of questions that student got wrong.
            print('Questions you answered incorrectly: ', end='')
            while counter < incorrect_count:
                print(incorrect_questions[counter], end='')
                if counter + 1 < incorrect_count:
                    print (', ', end='')
                counter += 1
                
    # Handle any errors that may occur.
    except FileNotFoundError:
        print('The file could not be found')
    except IOError:
        print('There was an IO error.')
    except IndexError:
        print('There was an indexing error')
    except:
        print('An error occurred')

# Call the main function.
if __name__ == '__main__':
    main()