import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator

class RoyalFlushValidatorTest(unittest.TestCase):
    def test_validates_cards_dont_have_straight_flush_ending_with_ace(self):
       cards = [
           Card('9','Clubs'),
           Card('10','Clubs'),
           Card('Jack','Clubs'),
           Card('Queen','Clubs'),
           Card('King','Clubs'),
           Card('Ace','Diamonds')
       ]
       validator = RoyalFlushValidator(cards)
       self.assertEqual(validator.is_valid(), False)

    def test_validates_cards_dont_have_straight_flush_ending_with_ace(self):
       cards = [
           Card('2','Spades'),
           Card('9','Clubs'),
           Card('10','Clubs'),
           Card('Jack','Clubs'),
           Card('Queen','Clubs'),
           Card('King','Clubs'),
           Card('Ace','Clubs'),
           Card('Ace','Diamonds')
       ]
       validator = RoyalFlushValidator(cards)
       self.assertEqual(validator.is_valid(), True)

    def test_gives_5_strightCards_with_samerank_ending_with_ace(self):
        cards = [
            Card('2','Diamonds'),
            Card('10','Clubs'),
            Card('Jack','Clubs'),
            Card('Queen','Clubs'),
            Card('King','Clubs'),
            Card('Ace','Clubs'),
            Card('Ace','Diamonds')
        ]
        validator = RoyalFlushValidator(cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                Card('10','Clubs'),
                Card('Jack','Clubs'),
                Card('Queen','Clubs'),
                Card('King','Clubs'),
                Card('Ace','Clubs'), 
            ]
        )