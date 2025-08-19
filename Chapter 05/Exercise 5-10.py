import random

# main function
def main():
    
    # Local variables
    QUESTIONS = 5
    LIMIT = 10

    # Repeat QUESTIONS times.
    for i in range(QUESTIONS):

        # Print the question number.
        print('Question', (i + 1))

        # Call generate_question and print the result.
        print(generate_question(LIMIT))

       
# The generate_question function accepts max_number
# and returns a string of an addition question of
# two numbers between 1 and max_number in the format
# "num1 + num2 = _____".
def generate_question(max_number):
    num1 = random.randint(1, max_number)
    num2 = random.randint(1, max_number)
    question = str(num1) + ' + ' + str(num2) + ' = _____\n'
    return question

    
# Call the main function.
main()
