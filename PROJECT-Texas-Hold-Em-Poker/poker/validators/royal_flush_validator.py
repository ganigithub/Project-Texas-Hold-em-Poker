from poker.validators import StraightFlushValidator

class RoyalFlushValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = 'Royal Flush'

    def is_valid(self):
        straight_flush_validator = StraightFlushValidator(self.cards)
        if straight_flush_validator.is_valid(): #we check if cards have straightflush
            straight_flush_cards  = straight_flush_validator.valid_cards() #we extract valid cards
            return straight_flush_cards[-1].rank == 'Ace'       #then check whether last rank is Ace
        return False

    def valid_cards(self):
        return StraightFlushValidator(cards=self.cards).valid_cards()
#since royalflush has only one possible combination, and since is_valid checks for royal combination,
#we simply return the valid_cards for straightflush.