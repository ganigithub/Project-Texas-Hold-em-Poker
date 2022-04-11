from logging import PlaceHolder
import unittest
from unittest import mock
from unittest.mock import MagicMock

from poker.card import Card
from poker.player import Player
from poker.hand import Hand

class PlayerTest(unittest.TestCase):
    def test_stores_cards_and_name(self):
        hand = Hand()
        player = Player(name = 'gani', hand = hand)
        
        self.assertEqual(player.name , 'gani')
        self.assertEqual(player.hand, hand)

    def test_figures_own_best_hand(self):
        mock_hand = MagicMock() #this will mock real hand object
        mock_hand.best_rank.return_value = 'Flush'  #we are setting the default returnvalue.

        player = Player(name = 'gani', hand = mock_hand)
        self.assertEqual(player.best_hand(),'Flush')
        
        mock_hand.best_rank.assert_called()

    def test_pass_new_cards_to_hand(self):
        mock_hand = MagicMock()
        player = Player(name='gani',hand=mock_hand)
        cards = [Card('2', 'Diamonds'),Card('Ace', 'Hearts')]

        player.add_cards(cards)
        mock_hand.add_cards.assert_called_once_with(cards)

    def test_decides_to_continue_or_drop_out_of_game(self):
        player = Player(name='gani',hand=Hand())
        self.assertEqual(player.wants_to_fold(),False)

    def test_is_sorted_by_best_hand(self):
        mock_hand1 = MagicMock()
        mock_hand1.best_rank.return_value = (0, 'Royal Flush', [])  #we dont care about list.

        mock_hand2 = MagicMock()
        mock_hand2.best_rank.return_value = (2, 'Four Of A Kind', [])

        player1 = Player('gani', mock_hand1)
        player2 = Player('garry', mock_hand2)
        players = [player1, player2]

        self.assertEqual(
            max(players),
            player1
        )
