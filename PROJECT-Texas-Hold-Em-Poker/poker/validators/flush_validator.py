class FlushValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = 'Flush Card'

    def is_valid(self):
        return len(self._suits_which_occur_more_than_5_times) == 1

    def valid_cards(self):
        cards = [card for card in self.cards if card.suit in self._suits_which_occur_more_than_5_times.keys()]
        return cards[-5:]   #returns the last 5 highest cards in cards list.

    @property
    def _suits_which_occur_more_than_5_times(self):
        return {
            suit : suit_count
            for suit, suit_count in self._card_suit_count.items()
            if  suit_count >= 5 
        }

    @property
    def _card_suit_count(self):
        card_suit_count = {}
        for card in self.cards:
            card_suit_count.setdefault(card.suit, 0)
            card_suit_count[card.suit] +=1
        return card_suit_count