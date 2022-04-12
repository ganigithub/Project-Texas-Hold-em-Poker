import unittest

from poker.card import Card
from poker.validators import FourOfAKindValidator

class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):        
        self.two_of_clubs = Card('2','Clubs')
        self.two_of_diamonds = Card('2','Diamonds')
        self.two_of_hearts = Card('2','Hearts')
        self.two_of_spades = Card('2','Spades')
        self.nine_of_hearts = Card('9','Hearts')
        
        self.cards = [
            self.two_of_hearts,
            self.two_of_diamonds,
            Card('5','Clubs'),
            self.two_of_hearts,
            self.two_of_spades,
            self.nine_of_hearts
        ]

    def test_validates_four_cards_have_same_rank(self):
        validator = FourOfAKindValidator(cards=self.cards)
        self.assertEqual(validator.is_valid(), True)

    def test_returns_4_cards_with_same_rank(self):
        validator = FourOfAKindValidator(cards=self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.two_of_hearts,
                self.two_of_diamonds,
                self.two_of_hearts,
                self.two_of_spades,
            ]
        )