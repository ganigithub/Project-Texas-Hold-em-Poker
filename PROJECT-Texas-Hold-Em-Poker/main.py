from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand
from poker.player import Player
from poker.game_round import GameRound

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()

player1 = Player(name = 'garry', hand = hand1)
player2 = Player(name = 'gani', hand = hand2)
players = [player1, player2]

gameround = GameRound(deck = deck, players = players )
gameround.play()

for player in players:
    print(f'{player.name} receives the cards {player.hand}.')
    index, hand_name, hand_cards = player.best_hand()
    hand_card_strings = [str(card) for card in hand_cards]
    hand_card_string = ' and '.join(hand_card_strings)
    print(f'{player.name} has a {hand_name} with cards {hand_card_string}.')

winning_player = max(players)

print(f'Winning player is {winning_player.name}')