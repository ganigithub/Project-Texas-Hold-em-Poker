class NoCardsValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = 'No Card'

    def is_valid(self):
        return len(self.cards) == 0

    def valid_cards(self):
        return self.cards[-1:]