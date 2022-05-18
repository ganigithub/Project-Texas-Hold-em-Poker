from poker.validators import RankValidator

class ThreeOfAKindValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = 'Three of a Kind'

    def is_valid(self):
        ranks_with_three_of_a_kind = self._ranks_with_count(3) #{'ace':3}
        return len(ranks_with_three_of_a_kind) == 1

    def valid_cards(self):
        ranks_with_three_of_a_kind = self._ranks_with_count(3)
        return [card for card in self.cards if card.rank in ranks_with_three_of_a_kind.keys()]