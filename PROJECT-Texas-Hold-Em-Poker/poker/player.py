## we use dependency injection in this case to avoid usind Hand Class directly in body of Player class
# dependency injection is used to 'seperate concerns' of 'using' and 'constructing'.
# by using dependency, we can direct a class/object to use another object without concerning about 
#its construction.

class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def best_hand(self):
        return self.hand.best_rank()

#we used dependency injection in here. The real Hand is not used.
# if we didn't used dependency injection, above line would look like Hand(self.cards).best_rank()
#which would couple the Hand and Player class. which we don't want.

    def add_cards(self, cards):
        self.hand.add_cards(cards)
#above method will call add_cards to hand whichin turn refers to gameround

    def wants_to_fold(self): 
        return False  #we can add logic where player can drop out but to keep simple, we keep false.

    def __gt__(self, other):
        current_player_best_validator_index = self.best_hand()[0]  # 0
        other_player_best_validator_index = other.best_hand()[0]  #2

        return current_player_best_validator_index < other_player_best_validator_index
        #since player with lower validator_index has upper hand, player will be considered greater