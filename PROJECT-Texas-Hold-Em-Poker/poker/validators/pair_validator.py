from poker.validators import RankValidator
#the _ranks_with_count() used in line 11 is stored in rank_validator file in poker.validators
#we inherit the class RankValidator.

class PairValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = 'Pair'

    def is_valid(self):
        ranks_with_pair = self._ranks_with_count(2) # {'10':2}
        return len(ranks_with_pair)==1
    
    def valid_cards(self):
        ranks_with_pair = self._ranks_with_count(2)
        return [card for card in self.cards if card.rank in ranks_with_pair.keys()]
