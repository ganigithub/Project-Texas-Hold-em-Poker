#we are going to create empty deck of cards and then add cards to it later

import random

class Deck():
    def __init__(self):
        self.cards = []
    
    def __len__(self):
        return len(self.cards)

    def add_cards(self, cards):
        self.cards.extend(cards)
#we use extend coz it adds any number of elements to list. While append adds only one object.

    def remove_cards(self, number):  #this removes the cards from deck when players are given cards at start.
        cards_to_remove = self.cards[:number]
        del self.cards[:number]
        return cards_to_remove

    def shuffle(self):
        random.shuffle(self.cards)