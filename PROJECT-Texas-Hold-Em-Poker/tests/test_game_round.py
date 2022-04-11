import unittest
from unittest.mock import MagicMock, call

from poker.card import Card
from poker.game_round import GameRound

class GameRoundTest(unittest.TestCase):
    def setUp(self):   #following cards will be used before every test
        self.first_two_cards = [Card('2','Hearts'),Card('Ace', 'Spades')] 
        self.next_two_cards = [Card('King', 'Clubs'),Card('4', 'Diamonds')]
        self.flop_cards = [Card('Ace','Hearts'),Card('3','Diamonds'),Card('Jack','Spades')]
    #community_cards will be shared by all players.
        self.turn_card = [Card('9','Hearts')]
        self.river_card = [Card('7','Clubs')]

    def test_stores_deck_and_players(self):
        deck = MagicMock()
        players = [MagicMock(), MagicMock()]

        game_round = GameRound(deck=deck, players=players)

        self.assertEqual(game_round.deck , deck)
        self.assertEqual(game_round.players, players)

    def test_game_play_shuffles_deck(self):  #shuffles deck before play
        mock_deck = MagicMock()
        players = [MagicMock(), MagicMock()]

        game_round = GameRound(deck=mock_deck, players=players)

        game_round.play()
        mock_deck.shuffle.assert_called_once_with()

    def test_deals_two_initial_cards_from_deck_to_each_player(self): #tests 2 cards r provided to each player

        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
            self.first_two_cards,
            self.next_two_cards,
            self.flop_cards,
            self.turn_card,
            self.river_card
            ]
        
        mock_player1 = MagicMock()
        mock_player2 = MagicMock()
        players = [mock_player1, mock_player2]

        game_round = GameRound(deck=mock_deck, players=players)
        
        game_round.play()
        mock_deck.remove_cards.assert_has_calls(
            [call(2), call(2)]
        )
        #that means remove_cards has be called 2 times with 2 as argument.
        #above line tests that remove_cards method has been called the same no of times as players.
        # 2 players, so 2 calls in this case.

        mock_player1.add_cards.assert_has_calls(
            [call(self.first_two_cards)]
            )
        mock_player2.add_cards.assert_has_calls(
            [call(self.next_two_cards)]
            )

    def test_removes_player_if_not_want_to_play(self):
        deck = MagicMock()
        player1 = MagicMock()
        player2 = MagicMock()
        
        player1.wants_to_fold.return_value = True
        player2.wants_to_fold.return_value = False
        
        players = [player1, player2]
        gameround = GameRound(deck=deck,players=players)
        gameround.play()
        self.assertEqual(gameround.players, [player2])

    def test_deals_each_player_flop_turn_river_cards(self):
        mock_player1 = MagicMock()
        mock_player1.wants_to_fold.return_value = False #if we don't set ret_value for wants_to_fold,
        # to False, it will be True for each player and will be removed. We don't want that

        mock_player2 = MagicMock()
        mock_player2.wants_to_fold.return_value = False
        players = [mock_player1, mock_player2]

        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
            self.first_two_cards,
            self.next_two_cards,
            self.flop_cards,
            self.turn_card,
            self.river_card]

        game_round = GameRound(deck=mock_deck,players=players)
        game_round.play()

        mock_deck.remove_cards.assert_has_calls(
            [call(3), call(1), call(1)]
            )
#above assertion tests that remove_cards has been invoked with the calls having
#arguments 3(flop cards), 1(turn card) & 1(river card)

        calls = [
            call(self.flop_cards),
            call(self.turn_card),
            call(self.river_card)]
        
        for player in players:
            player.add_cards.assert_has_calls(calls)
# in above assertion, we test that each player has invoked add_card with calls list arguments.