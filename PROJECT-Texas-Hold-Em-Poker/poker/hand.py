from poker.validators import (
    RoyalFlushValidator,
    StraightFlushValidator,
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator,
    HighCardValidator,
    NoCardsValidator,
)

class Hand():
    def __init__(self):
        self.cards = []
    
    def __repr__(self):   #gives cards in string format
        cards_as_strings = [str(card) for card in self.cards]
        return ', '.join(cards_as_strings)

    def add_cards(self, cards):
        copy = self.cards[:] #we create copy coz sort below will mutate orginal cards & we don't want that
        copy.extend(cards)
        copy.sort()          #we sort the cards that we get in hand acc to their ranks
        self.cards = copy

# we can see Hand and Deck are doing same thing: storing cards at this point. So you might think to merge them.
# But 'Duplication is cheaper(easy to fix) than wrong abstraction'. Means if we merge Hand and Deck,
#later on, it might become too complex and too many responsibilities on one file. Which might be
#disadvantageous for us. Hand and Deck looks same but futher they have different responsibilities.
# So we should avoid premature Refactoring.

    VALIDATORS = (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator,
        HighCardValidator,
        NoCardsValidator,
    )

    def best_rank(self):
        for validator_index, validator_klass in enumerate(self.VALIDATORS):
            validator = validator_klass(cards = self.cards)
            if validator.is_valid():
                return (validator_index, validator.name, validator.valid_cards())
