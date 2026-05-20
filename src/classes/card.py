from utils.constants import RANK_NAMES

class Card:
    """Card class is a simple class that represents a card."""
    def __init__(self, rank: int, suit: str):
        self.rank = rank
        self.suit = suit
        self.value = self.rank + 2 # Adjust since rank is 0 indexed
        if self.value > 10:
            self.value = 10

    def __repr__(self):
        return f'{RANK_NAMES[self.rank]} of {self.suit}'