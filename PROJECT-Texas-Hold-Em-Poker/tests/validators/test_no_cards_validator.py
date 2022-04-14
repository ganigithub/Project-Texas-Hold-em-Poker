import unittest

from poker.card import Card
from poker.validators import NoCardsValidator

class NoCardsValidatorTest(unittest.TestCase):
    def test_validates_no_cards_are_present(self):
        
        validator = NoCardsValidator(cards = [])
        self.assertEqual(validator.is_valid(), True)
        self.assertEqual(validator.valid_cards(), [])