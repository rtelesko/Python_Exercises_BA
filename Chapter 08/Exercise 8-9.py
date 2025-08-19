# Programming Exercise 8-9

def main():
    # Local variables
    vowels = 0
    consonants = 0

    # Get the string as input from the user.
    user_string = input('Enter a string: ')

    # Call the vowel_counter function,
    # storing the result.
    vowels = vowel_counter(user_string)
    
    # Call the consonant_counter function,
    # storing the result.
    consonants = consonant_counter(user_string)

    # Display the results.
    print(f'The string you entered includes {vowels} '
          f'vowels and {consonants} consonants.')

# The vowel_counter method receives a string and
# returns the number of vowels in the string.
def vowel_counter(string):
    # Set up local variables
    count = 0
    vowels = 'aeiou'

    # For each character,
    # determine if it is a vowel.
    for ch in string:
        if vowels.find(ch) >= 0:
            count = count + 1

    # Return the number of vowels in the string.
    return count
        
# The consonant_counter method receives a string and
# returns the number of consonants in the string.
def consonant_counter(string):
    # Set up local variables
    count = 0
    consonants = 'bcdfghjklmnpqrstvwxyz'

    # For each character,
    # determine if it is a consonant.
    for ch in string:
        if consonants.find(ch) >= 0:
            count = count + 1

    # Return the number of consonants in the string.
    return count

# Call the main function.
if __name__ == '__main__':
    main()