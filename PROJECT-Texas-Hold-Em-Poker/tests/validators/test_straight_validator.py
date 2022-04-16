import unittest

from poker.card import Card
from poker.validators import StraightValidator

class StraightValidatorTest(unittest.TestCase):

    def setUp(self):
        self.two = Card('2','Clubs')
        self.six = Card('6', 'Spades')
        self.seven = Card('7', 'Clubs')
        self.eight = Card('8', 'Hearts')
        self.nine = Card('9', 'Diamonds')
        self.ten = Card('10', 'Diamonds')
        self.jack = Card('Jack', 'Hearts')

        self.cards = [
            self.two,
            self.six,
            self.seven,
            self.eight,
            self.nine,
            self.ten,
            self.jack
        ]

    def test_tells_if_there_are_five_cards_in_row(self):
        validator = StraightValidator(cards=self.cards)
        self.assertEqual(validator.is_valid(), True)

    def test_give_5_highest_cards_in_row(self):
        validator = StraightValidator(cards=self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.seven,
                self.eight,
                self.nine,
                self.ten,
                self.jack
            ]
        )
    def test_does_not_deems_two_cards_as_straight(self):
        cards = [Card('2','Hearts'), Card('3','Hearts')]
        validator = StraightValidator(cards=cards)
        self.assertEqual(validator.is_valid(), False)