from poker.validators import FiveCardRanksInRowValidator

class StraightValidator(FiveCardRanksInRowValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = 'Straight Card'
    
    def is_valid(self):
        # if len(self.cards) < 5:  #we dont need to write this coz while loop in line23 will not work
        #     return False         #if there are cards less than 5
        
        return len(self._collections_of_5_straight_cards_in_row) >= 1

    def valid_cards(self):
        return self._collections_of_5_straight_cards_in_row[-1]       