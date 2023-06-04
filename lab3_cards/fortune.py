def faith(card):
    if card.suit == cards.SuitEnum.hearts:
        return '''You picked Hearts. Probably you will face some conflict soon.'''
    elif card.suit == cards.SuitEnum.diamonds:
        return '''You picked Diamonds. You will get an unforseen reward.'''
    elif card.suit == cards.SuitEnum.clubs:
        return '''You picked Clubs. There will be some joy very soon.'''
    elif card.suit == cards.SuitEnum.spades:
        return '''You picked Spades. Beware of betrayal.'''

TIP = '''Please use these arguments:
        decktype = 36 or 52 cards
        cards_count = how many cards to pick'''

def main(args):

    if len (args) > 3:
        exit (f'Too many arguments. \n{TIP}\n')   
    elif len (args) < 3:
        exit (f'Too less arguments. \n{TIP}\n')
    else:
        decktype = int(args[1])
        cards_count = int(args[2])

    if decktype == 36:
        deck = cards.FrenchDeck36()
    else:
        deck = cards.FrenchDeck52()

    print('Taking a card...')

    for i in range (0, cards_count):
        card = deck.check_card_by_index(i)
        print(faith(card))

    return 0

if __name__ == '__main__':
    import sys
    import random
    import cards
    sys.exit(main(sys.argv))
