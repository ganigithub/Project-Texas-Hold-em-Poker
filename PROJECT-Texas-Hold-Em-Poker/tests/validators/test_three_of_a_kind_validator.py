import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.five_of_clubs    = Card(rank = "5", suit = "Clubs")
        self.king_of_clubs    = Card(rank = "King", suit = "Clubs")
        self.king_of_diamonds = Card(rank = "King", suit = "Diamonds")
        self.king_of_hearts   = Card(rank = "King", suit = "Hearts")
        self.ace_of_spades    = Card(rank = "Ace", suit = "Spades")

        self.cards = [
            self.five_of_clubs,
            self.king_of_clubs,
            self.king_of_diamonds,
            self.king_of_hearts,
            self.ace_of_spades
        ]

    def test_validates_cards_have_exactly_three_cards_of_same_rank(self):
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(validator.is_valid(), True)

    def test_returns_threeofakind_cards_from_collection(self):
        validator = ThreeOfAKindValidator(cards = self.cards)
        
        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_clubs,
                self.king_of_diamonds,
                self.king_of_hearts
            ]
        )