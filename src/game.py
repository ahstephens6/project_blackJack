from classes.player import Player
from classes.deck import Deck
from classes.game import Game


def setup_player() -> Player:
    """Get player name and create player object"""
    name = input('What is your name? ')
    return Player(name)


def setup_deck() -> Deck:
    """Ask for the number of decks in the shoe and then create it."""
    number_decks = int(input('How many decks in the shoe? '))
    return Deck(number_decks)


def create_game(player: Player, deck: Deck) -> Game:
    """Create the game object than handles playing the game.
    
    Parameters
    ----------
    player: Player - The player in the game
    deck: Deck - The deck for the game
    
    Returns
    ------
    Game"""
    return Game(player, deck)


if __name__ == '__main__':
    player = setup_player()
    deck = setup_deck()
    game = create_game(player, deck)
    game.start()
