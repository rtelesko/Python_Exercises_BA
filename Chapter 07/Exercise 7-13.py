import random

# Magic 8 Ball Program

def main():
    # Open the 8 Ball Response file.
     with open('8_ball_responses.txt', 'r') as response_file:
        # Read the file contents into a list.
        responses = response_file.readlines()

        # Strip the newline from each element.
        for i in range(len(responses)):
            responses[i] = responses[i].rstrip('\n')

        # Get the user's question.
        question = input('Enter your question: ')

        # Display a random response.
        print(responses[random.randint(0, len(responses))])

# Call the main function.
if __name__ == '__main__':
    main()