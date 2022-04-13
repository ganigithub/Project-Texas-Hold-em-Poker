import unittest

from poker.card import Card

from poker.validators import HighCardValidator
#above line will not import HighCardValidator class directly into this file.
#coz poker.validators is a whole package not specific file.
#we can still use this syntax only by importing those specific files in _init_.py file of validators package

class HighCardValidatorTest(unittest.TestCase):
    def test_validates_high_card(self):

        cards = [Card('2', 'Clubs'), Card('Ace', 'Spades')]
#the cards we get will always come sorted coz of Hand class
# so we dont need to wory for validators to sort cards
        
        validator = HighCardValidator(cards = cards)

        self.assertEqual(validator.is_valid(), True)

    def test_returns_high_card_from_card_collection(self):
        ace_of_diamonds = Card('Ace','Diamonds')
        cards = [
            Card('2','Hearts'),
            Card('6','Diamonds'),
            Card('7','Hearts'),
            Card('King','Spades'),
            ace_of_diamonds
        ]
        validator = HighCardValidator(cards)

        self.assertEqual(
            validator.valid_cards(),
            [ace_of_diamonds])