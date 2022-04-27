class FiveCardRanksInRowValidator():
    @property
    def _collections_of_5_straight_cards_in_row(self):
        index = 0
        final_index = len(self.cards) - 1  # 6
        collections_of_5_straight_cards_in_row = []

        while index + 4 <= final_index:
            next_five_cards = self.cards[index : index + 5]
            next_five_rank_indices = [card.rank_index for card in next_five_cards]

            if self._every_element_increasing_by_1(next_five_rank_indices):
                collections_of_5_straight_cards_in_row.append(next_five_cards)

            index += 1
        
        return collections_of_5_straight_cards_in_row

    def _every_element_increasing_by_1(self, rank_indexes):
        starting_rank_index = rank_indexes[0]
        last_rank_index     = rank_indexes[-1]
        straight_consecutive_indexes = list(
            range(starting_rank_index, last_rank_index + 1)
        )
        return rank_indexes == straight_consecutive_indexes