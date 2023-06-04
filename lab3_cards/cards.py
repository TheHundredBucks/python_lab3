import itertools
import random
from enum import Enum

class SuitEnum(Enum):

    spades    = '\u2660'
    hearts    = '\u2665'
    diamonds  = '\u2666'
    clubs     = '\u2663'

    def __str__(cls):
        return f'{cls.name} ({cls.value})'

class RankEnum(Enum):

    one   = 1
    two   = 2
    three = 3
    four  = 4
    five  = 5
    six   = 6
    seven = 7
    eight = 8
    nine  = 9
    ten   = 10
    jack  = 'J'
    queen = 'Q'
    king  = 'K'
    ace   = 'A'

    def __str__(cls):
        return f'{cls.name} ({cls.value})'

class Card:
    __slots__ = 'rank', 'suit'  # consume less memory

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def info(self):
        return f'{self.rank.name()} of {self.suit.name}'

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.rank} of {self.suit}>'


class CardDeckBase:
    __slots__ = 'cards'  # consume less memory
    
    def __init__(self):
        self.cards = list()
        
    def check_card_by_index(self, index):
        return self.cards[index]

    def list_cards(self):
        for el in self.cards:
            print(el)

    def card_remix(self):
        random.shuffle(self.cards)
    
    def __repr__(self):
        return f'<{self.__class__.__name__}: card deck>'
    
class FrenchDeck52(CardDeckBase):
    
    def __init__(self):
        super().__init__()
        
        products = itertools.product(list(RankEnum), list(SuitEnum))
        for el in products:
            self.cards.append(Card(el[0], el[1]))

        self.card_remix()

class FrenchDeck36(CardDeckBase):
    
    def __init__(self):
        super().__init__()
        
        products = itertools.product(list(RankEnum)[5:], list(SuitEnum))
        for el in products:
            self.cards.append(Card(el[0], el[1]))

        self.card_remix()

if __name__ == '__main__':
    ...
