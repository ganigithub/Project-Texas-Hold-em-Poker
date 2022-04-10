import unittest
from poker.card import Card

class CardTest(unittest.TestCase):
    def test_rank(self):
        card = Card(rank = 'Queen', suit = 'Hearts')
        self.assertEqual(card.rank , 'Queen')
    
    def test_suit(self):
        card = Card(rank = '2', suit = 'Clubs')
        self.assertEqual(card.suit, 'Clubs')
#
    def test_knows_its_rank_index(self):
        card = Card(rank = 'Jack', suit = 'Clubs')
        self.assertEqual(card.rank_index, 9)

    def test_has_string_representation_with_rank_and_suit(self):
        card = Card(rank = '5', suit = 'Diamonds')
        self.assertEqual(str(card), '5 of Diamonds')

    def test_has_technical_representation(self): #tells how an object should be instantiated
        card = Card(rank = '5', suit = 'Diamonds')
        self.assertEqual(repr(card), "Card('5', 'Diamonds')")
#
    def test_card_has_four_possible_suit_options(self):
        self.assertEqual(
            Card.SUITS,
            ('Hearts', 'Diamonds', 'Clubs', 'Spades')
        )

    def test_card_has_thirteen_possible_rank_options(self):
        self.assertEqual(
            Card.RANKS,
            ('2','3','4','5','6','7','8','9','10',
            'Jack', 'Queen', 'King', 'Ace')
        )
    
    def test_card_only_allows_for_valid_suits(self):
        with self.assertRaises(ValueError):
            Card(rank = 'Two', suit = 'Queen')
    
    def test_card_only_allow_for_valid_ranks(self):
        with self.assertRaises(ValueError):
            Card(rank = '2', suit = 'Dots')
#
    def test_can_create_52_cards(self):
        cards = Card.create_standard_52_cards()
        self.assertEqual(len(cards), 52)

        #we dont need to instantiate and check whole 52 cards. We just need to check first and last
        self.assertEqual(cards[0], Card(rank='2', suit='Hearts'))
        self.assertEqual(cards[-1], Card(rank='Ace',suit='Spades'))

    def test_considers_two_cards_equal_if_same_RankSuit(self):
        self.assertEqual(
            Card(rank = '2', suit = 'Hearts'),
            Card(rank = '2', suit = 'Hearts')
        )
#
    def test_card_sort_itself_with_other_card(self):
        king_of_spades = Card('King','Spades')
        queen_of_clubs = Card('Queen','Clubs')
        evaluation = queen_of_clubs < king_of_spades
        self.assertEqual(evaluation, True)

    def test_sorts_cards(self):
        two_of_spades = Card('2','Spades')
        five_of_diamonds = Card('5','Diamonds')
        five_of_hearts = Card('5','Hearts')
        eight_of_hearts = Card('8','Hearts')
        ace_of_clubs = Card('Ace','Clubs')

        unsorted_cards = [
            eight_of_hearts,
            two_of_spades,
            ace_of_clubs,
            five_of_diamonds,
            five_of_hearts
        ]

        unsorted_cards.sort()

        self.assertEqual(
            unsorted_cards,
            [
                two_of_spades,
                five_of_diamonds,
                five_of_hearts,
                eight_of_hearts,
                ace_of_clubs
            ]
        )