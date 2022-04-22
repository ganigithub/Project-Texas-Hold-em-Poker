
class GameRound():
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players
    
    def _shuffle_deck(self):   #shuffles deck cards
        self.deck.shuffle()

    def _deal_initial_two_cards_to_each_player(self):
        for player in self.players:
            two_cards = self.deck.remove_cards(2)
            player.add_cards(two_cards)
    
#in above code, we are adding the same two cards that we are removing from deck to each player.

    def _make_bets(self):    #tests whether player wants to continue or drop
        for player in self.players:
            if player.wants_to_fold():
                self.players.remove(player)

    def _gives_community_cards(self, number):
        community_cards = self.deck.remove_cards(number)
        for player in self.players:
            player.add_cards(community_cards)

    def _gives_flop_cards(self):      #gives 3 flop cards to player
        self._gives_community_cards(3)
        
    def _gives_turn_card(self):        #gives 1 turn card to player
        self._gives_community_cards(1)

    def _gives_river_card(self):       #gives 1 river card to player
        self._gives_community_cards(1)

    def play(self):   #invokes following methods in body sequentially
        self._shuffle_deck()
        self._deal_initial_two_cards_to_each_player()
        self._make_bets()

        self._gives_flop_cards()
        self._make_bets()
        
        self._gives_turn_card()
        self._make_bets()
        
        self._gives_river_card()
        self._make_bets()