class Card():
    SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    RANKS = ('2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace')

    def __init__(self, rank, suit):       
        self.rank = rank
        self.suit = suit
        self.rank_index = self.RANKS.index(rank) #gives rank idx for each card
        
        if rank not in self.RANKS:
            raise ValueError(f'Invalid Rank. Rank must be from {self.RANKS}')        
        if suit not in self.SUITS:
            raise ValueError(f'Invalid Suit. Suit must be from {self.SUITS}')
#
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def __repr__(self):         #tells how object should be instantiated
        return f"Card('{self.rank}', '{self.suit}')"

    def __eq__(self, other_card):
        return self.rank==other_card.rank and self.suit==other_card.suit
#we need to define above equality coz python considers elemnts with same rank and suit different
#coz they hold different memory.
# you can check this functionality in your main.py playground

    def __lt__(self,other):  #(less than)tells if one card is less than other card
        if self.rank == other.rank:
            self.suit < other.suit
        return self.rank_index < other.rank_index
        
#we declare 52 cards in Card because Deck will interfere in Card too much if we declared 52cards in Deck.
    @classmethod
    def create_standard_52_cards(cls):
        # cards = []
        # for suit in cls.SUITS:
        #     for rank in cls.RANKS:
        #         cards.append(cls(rank=rank, suit=suit))
        # return cards
#we can use below list comprehension instead of above lines23-27
        return [
            cls(rank=rank, suit=suit)
            for suit in cls.SUITS
            for rank in cls.RANKS
        ]
    
