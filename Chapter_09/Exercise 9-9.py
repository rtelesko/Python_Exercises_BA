# Programming Exercise 9-9

# Global constant for the winning number of cards
MAX = 21

# main function
def main():
    # Local variables
    hand1 = 0
    hand2 = 0
    deck = create_deck()

    while hand1 <= MAX and hand2 <= MAX:

        # Deal a card to each player and calculate hand value.
        card1, value1 = deck.popitem()
        hand1 = update_hand_value(hand1, value1, card1)
    
        card2, value2 = deck.popitem()
        hand2 = update_hand_value(hand2, value2, card2)

        print(f'Player 1 was dealt {card1}')
        print(f'Player 2 was dealt {card2}')
        print()

    # Determine the winner.
    if hand1 > MAX and hand2 > MAX:
        print("There is no winner.")
    elif hand1 > 21:
        print("Player 2 wins.")
    else:
        print("Player 1 wins.")

# The create_deck function creates a deck of cards and
# returns the deck.
def create_deck():
    # Set up local variables
    suits = ['Spades','Hearts','Clubs','Diamonds']
    special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10}

    # Create list of all the card values
    numbers = ['Ace', 'King', 'Queen', 'Jack']
    for i in range(2,11):
        numbers.append(str(i))

    # Initialize deck
    deck = {}
    for suit in suits:
        for num in numbers:
            # Values 2-10.
            if num.isnumeric(): 
                deck[num + ' of ' + suit] = int(num)
            # Ace, King, Queen, or Jack.
            else: 
                deck[num + ' of ' + suit] = special_values[num]
    return deck

def update_hand_value(hand, value, card):
    if not card.startswith('Ace'):
        return hand+value
    # Adding 11 would cause to go over the maximum.
    elif hand > 10:
        # Value is 1 by default.
        return hand + value 
    else: 
        return hand + 11

# Call the main function.
if __name__ == '__main__':
    main()