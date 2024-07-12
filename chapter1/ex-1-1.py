"""
파이썬 카드 한 벌
Topic: Magic method __getitem__(), __len__()
"""

import doctest
import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        """
        >>> deck = FrenchDeck()
        >>> len(deck)
        52
        """
        return len(self._cards)

    def __getitem__(
        self, position
    ):  # __getitem__ 구현 -> FrenchDeck 클래스는 시퀀스처럼 동작 (membershop test)
        """
        >>> deck = FrenchDeck()
        >>> deck[0]
        Card(rank='2', suit='spades')
        >>> deck[3:5]
        [Card(rank='5', suit='spades'), Card(rank='6', suit='spades')]
        >>> deck[-1]
        Card(rank='A', suit='hearts')
        >>> deck[12::13]
        [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
        >>> for card in deck:  # doctest: +ELLIPSIS
        ...     print(card)
        Card(rank='2', suit='spades')
        Card(rank='3', suit='spades')
        ...
        Card(rank='A', suit='hearts')
        >>> for card in reversed(deck):  # doctest: +ELLIPSIS
        ...     print(card)
        Card(rank='A', suit='hearts')
        Card(rank='K', suit='hearts')
        ...
        Card(rank='2', suit='spades')
        >>> hamster_card = Card('7', 'hamster')
        >>> hamster_card
        Card(rank='7', suit='hamster')
        >>> hamster_card in deck
        False
        >>> real_card = Card('6', 'clubs')
        >>> real_card
        Card(rank='6', suit='clubs')
        >>> real_card in deck
        True
        """
        return self._cards[position]


doctest.testmod()
