import unittest

from poker.card import Card
from poker.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.two_of_clubs = Card('2', 'Clubs')
        self.two_of_diamonds = Card('2', 'Diamonds')
        self.five_of_clubs = Card('5', 'Clubs')
        self.ace_of_hearts = Card('Ace', 'Hearts')
        self.ace_of_spades = Card('Ace', 'Spades')

        self.cards = [
            self.two_of_clubs,
            self.two_of_diamonds,
            self.five_of_clubs,
            self.ace_of_hearts,
            self.ace_of_spades
        ]

    def test_figures_out_cards_have_atleast_two_pairs_of_samerank(self):        
        validator = TwoPairValidator(cards = self.cards)
        self.assertEqual(validator.is_valid(), True)

    def test_returns_two_pairs_of_cards_from_collection(self):
        validator = TwoPairValidator(cards = self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.two_of_clubs,
                self.two_of_diamonds,
                self.ace_of_hearts,
                self.ace_of_spades
            ]
        )