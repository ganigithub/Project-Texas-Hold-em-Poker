import unittest

from poker.card import Card
from poker.validators import FullHouseValidator

class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self):
        self.two_of_clubs = Card('2','Clubs')
        self.two_of_diamonds = Card('2','Diamonds')
        self.two_of_hearts = Card('2','Hearts')
        self.nine_of_hearts = Card('9','Hearts')
        self.nine_of_spades = Card('9','Spades')

        self.cards = [
            self.two_of_clubs,
            self.two_of_diamonds,
            self.two_of_hearts,
            Card('5','Diamonds'),
            self.nine_of_hearts,
            self.nine_of_spades
            ]

    def test_validates_2_cards_have_samerank_and_3_cards_have_samerank(self):
        validator = FullHouseValidator(cards = self.cards)
        self.assertEqual(validator.is_valid(), True)

    def test_returns_collection_of_2_cards_of_samerank_and_3_cards_of_samerank(self):
        validator = FullHouseValidator(cards=self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.two_of_clubs,
                self.two_of_diamonds,
                self.two_of_hearts,
                self.nine_of_hearts,
                self.nine_of_spades  
            ]
        )