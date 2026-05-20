from utils.constants import RANK_NAMES

class Card:
    """Card class is a simple class that represents a card."""
    def __init__(self, rank: int, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        print(f'{RANK_NAMES[self.rank]} of {self.suit}')