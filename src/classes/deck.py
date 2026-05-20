from card import Card
from utils.constants import SUITS

class Deck:
    """Class that handles the cards."""
    def __init__(self, num_decks: int = 0) -> None:
        """Constructor that tells how many decks will be in the shoe."""
        self.deck = Deck.build_deck(num_decks)
        

    @staticmethod
    def build_deck(num: int) -> list[Card]:
        """Static method for creating a deck.
        
        Parameter
        ---------
        num: int - Number of decks in the shoe"""
        ranks = [i for i in range(13)]
        
        deck = []
        for _ in range(num):
            for rank in ranks:
                for suit in SUITS:
                    deck.append(Card(rank, suit))
        return deck
        