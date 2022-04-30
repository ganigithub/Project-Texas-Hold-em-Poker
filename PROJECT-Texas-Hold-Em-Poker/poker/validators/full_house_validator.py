from poker.validators import ThreeOfAKindValidator, PairValidator

class FullHouseValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = 'Full House'
    
    def is_valid(self):
        return ThreeOfAKindValidator(cards=self.cards).is_valid() and PairValidator(cards=self.cards).is_valid()

    def valid_cards(self):
        three_of_a_kind_cards = ThreeOfAKindValidator(self.cards).valid_cards()
        pair_cards = PairValidator(self.cards).valid_cards()
        
        full_house_cards = (three_of_a_kind_cards + pair_cards)
        
        full_house_cards.sort()
        return full_house_cards