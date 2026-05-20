from classes.player import Player
from classes.deck import Deck

class Game:
    """Class for handling gamestate"""
    def __init__(self, player: Player, deck: Deck):
        """Constructor
        
        Parameters
        ---------
        player: Player - The player for the blackjack game
        deck: Deck - The deck for the blackjack game"""
        self.player = player
        self.deck = deck
        
    def start(self):        
        # Shuffle the cards
        # Move into the main game loop
        for card in self.deck.card_deck:
            print(f'{card}')
