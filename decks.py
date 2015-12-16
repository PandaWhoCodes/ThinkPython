import random


class Card(object):
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    # inside class Card:
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self, other):
        # check the suits

        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)

    def sort(self):
        return self.cards.sort()


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

                # inside class Deck:

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    # inside class Deck:
    def pop_card(self):
        return self.cards.pop()

    # inside class Deck:
    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        return random.shuffle(self.cards)

    # inside class Deck:
    def move_cards(self, hand, num):

        for i in range(num):
            hand.add_card(self.pop_card())

    """def deal_hands(self, nhands, n):
        for i in range(nhands):
            for j in range(n):
                self.hand.add_card(self.pop_card())

        print(self.hand)"""


class Hand(Deck):
    """Represents a hand of playing cards."""

    # inside class Hand:
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def find_defining_class(obj, method_name):

        """Finds and returns the class object that will provide
        the definition of method_name (as a string) if it is
        invoked on obj.

        obj: any python object
        method_name: string method name
        """
        for ty in type(obj).mro():
            if method_name in ty.__dict__:
                return ty
        return None


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    print (hand.find_defining_class(hand, 'shuffle'))

    deck.move_cards(hand, 5)
    hand.sort()
    print(hand)
