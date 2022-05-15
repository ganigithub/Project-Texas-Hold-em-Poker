class RankValidator():
    def _ranks_with_count(self, count): #filters our ranks with specific count
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }

    @property
    def _card_rank_counts(self): #gives dict with ranks and their count
        card_rank_count = {}
        for card in self.cards:
            card_rank_count.setdefault(card.rank, 0) #since dict is empty value of card.rank will be 0
            card_rank_count[card.rank] += 1 #now since card.rank is added in dict, its value will be 1
            # if card.rank repeats itself, count will be increased to 2.
        return card_rank_count
