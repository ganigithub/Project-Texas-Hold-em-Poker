import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    def test_determines_there_are_not_5_consicutive_cards_with_same_suits(self):
        cards = [
            Card('5','Clubs'),
            Card('6', 'Clubs'),
            Card('7', 'Clubs'),
            Card('8', 'Clubs'),
            Card('9', 'Hearts'),
            Card('10', 'Clubs'),
            Card('Jack', 'Hearts')
        ]
        self.jack = Card('Jack', 'Hearts')
        validator = StraightFlushValidator(cards=cards)
        self.assertEqual(validator.is_valid(), False)

    def test_determines_there_are_5_consicutive_cards_with_same_suits(self):
        cards = [
            Card('5','Clubs'),
            Card('6', 'Clubs'),
            Card('7', 'Clubs'),
            Card('8', 'Clubs'),
            Card('9', 'Clubs'),
            Card('10', 'Clubs'),
            Card('Jack', 'Hearts')
        ]
        self.jack = Card('Jack', 'Hearts')
        validator = StraightFlushValidator(cards=cards)
        self.assertEqual(validator.is_valid(),True)

    def test_determines_there_are_5_consicutive_cards_with_same_suits(self):
        five = Card('5','Clubs')
        six = Card('6', 'Clubs')
        seven = Card('7', 'Clubs')
        eight = Card('8', 'Clubs')
        nine = Card('9', 'Clubs')
        ten = Card('10', 'Clubs')
        jack = Card('Jack', 'Hearts')

        cards = [five,six,seven,eight,nine,ten,jack]

        validator = StraightFlushValidator(cards=cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                six,
                seven,
                eight,
                nine,
                ten
            ]
        )