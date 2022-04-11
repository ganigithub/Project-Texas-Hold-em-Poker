import unittest
from poker.card import Card
from poker.hand import Hand
from poker.validators import PairValidator

class HandTest(unittest.TestCase):

    def test_hand_starts_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards , [])

    def test_shows_all_cards_in_technical_representation(self):
        cards = [Card('3','Hearts'),Card('Ace','Clubs')]
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            repr(hand),
            '3 of Hearts, Ace of Clubs'
        )
    def test_receives_and_stores_cards(self):
        cards = [Card('2', 'Clubs'), Card('Ace', 'Spades')]
        hand = Hand()
        hand.add_cards(cards)
        
        self.assertEqual(hand.cards, cards)

    def test_interacts_with_validator_to_get_winning_hand(self):  #checks for validations of specific hand
        class HandWithOneValidator(Hand):
            VALIDATORS = (PairValidator, )  #we are overwriting the VALIDATOR with only one validator
                                            #instead of going through each validator.
                                            #comma is needed to create tuple of one element.
        ace_of_hearts = Card('Ace','Hearts')
        ace_of_spades = Card('Ace', 'Spades')
        cards = [ace_of_hearts, ace_of_spades]

        hand = HandWithOneValidator()
        hand.add_cards(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            (0,'Pair', [ace_of_hearts, ace_of_spades])
        )