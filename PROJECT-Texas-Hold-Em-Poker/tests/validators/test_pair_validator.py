import unittest

from poker.card import Card
from poker.validators import PairValidator

class PairValidatorTest(unittest.TestCase):
    def test_validates_cards_have_one_pair(self):
        cards = [Card('Ace','Spades'),Card('Ace','Diamonds')]
        validator = PairValidator(cards = cards)
        
        self.assertEqual(validator.is_valid(), True)

    def test_returns_pair_from_cards_collection(self):
        ten_of_clubs = Card('10', 'Clubs')
        ten_of_spades = Card('10','Spades')
        cards = [
            Card('2','Spades'),
            Card('3','Clubs'),
            Card('5','Hearts'),
            ten_of_clubs,
            ten_of_spades
        ]
        validator = PairValidator(cards)
        
        self.assertEqual(
            validator.valid_cards(),
            [ten_of_clubs, ten_of_spades]
        )