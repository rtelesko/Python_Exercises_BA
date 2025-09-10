# Programming Exercise 8-10

# Program displays the character that appears most frequently
# in the string. If several characters have the same highest
# frequency, displays the first character with that frequency.

def main():

    # Set up local variables
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = 0
    frequent = 0

    # Receive user input.
    user_string = input('Enter a string: ')

    for ch in user_string:

        ch = ch.upper()

        # Determine which letter this character is.
        index = letters.find(ch)
        if index>=0:

            # Increase counting array for this letter.
            count[index] = count[index] + 1

    for i in range(len(count)):
        if count[i] > count[frequent]:
            frequent = i

    print(f'The character that appears most frequently '
          f'in the string is {letters[frequent]}.')

# Call the main function.
if __name__ == '__main__':
    main()