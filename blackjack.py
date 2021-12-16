from random import shuffle, choice, randint

suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
numbers = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'}
deck = []

for suit in suits:
    for card in numbers:
        deck.append(card)
shuffle(deck)

def blackjack():
    yourCards = []
    compCards = []
    # name = input('What is your name?')

    i = 0
    while i < 2:
        yourCards.append(choice(deck))
        compCards.append(choice(deck))
        i += 1
    print(f'Your cards are {yourCards}')
    print(f"Computer's first card: {compCards[0]}")
    yourTotal = 0
    compTotal = 0
    for card in yourCards:
        if type(card) == int:
            yourTotal += card
        elif card == 'Jack' or card == 'King' or card == 'Queen':
            yourTotal += 10
        elif card == 'Ace':
            yourTotal += 11
    for card in compCards:
        if type(card) == int:
            compTotal += card
        elif card == 'Jack' or card == 'King' or card == 'Queen':
            compTotal += 10
        elif card == 'Ace':
            compTotal += 11

    if compTotal < 21:
                # comp_another_card = randint(0,1)
                # print(f'comp another card? {comp_another_card}')
                if compTotal <= 17:
                    next_comp_card = choice(deck)
                    compCards.append(next_comp_card)
                    if type(next_comp_card) == int:
                        compTotal += next_comp_card
                    elif next_comp_card == 'Jack' or card == 'King' or card == 'Queen':
                        compTotal += 10
                    elif next_comp_card == 'Ace':
                        if compTotal + 11 <= 21:
                            compTotal += 11
                        else:
                            compTotal += 1
                    # print(f'next comp card = {next_comp_card}')
    another_card = 'y'
    while yourTotal < 21 and another_card == 'y':
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        
        if another_card == 'y':
            next_card = choice(deck)
            yourCards.append(next_card)

            if type(next_card) == int:
                yourTotal += next_card
            elif next_card == 'Jack' or card == 'King' or card == 'Queen':
                yourTotal += 10
            elif next_card == 'Ace':
                if yourTotal + 11 <= 21:
                    yourTotal += 11
                else:
                    yourTotal += 1

            print(f'Your cards are {yourCards}')

    print(f'Computer\'s card are: {compCards}, (Comp total: {compTotal})')
        

    if yourTotal > compTotal and yourTotal < 22:
        print('You win!')
    elif compTotal > yourTotal and compTotal < 22:
        print('Computer wins!')
    elif yourTotal > 21:
        print('You lose!')
    elif compTotal > 21:
        print('Computer loses!')
    elif yourTotal == compTotal:
        print('Isssa tie!')
    again = input('Would you like to play again? \'yes\' or \'no\'')
    if again == 'yes':
        blackjack()

blackjack()