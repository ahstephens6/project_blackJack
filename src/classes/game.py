from classes.player import Player
from classes.deck import Deck

from utils.constants import PLAYER_CHOICES

class Game:
    """Class for handling gamestate"""
    def __init__(self, player: Player, deck: Deck):
        """Constructor
        
        Parameters
        ---------
        player: Player - The player for the blackjack game
        deck: Deck - The deck for the blackjack game"""
        self.player = player
        self.dealer = Player('Dealer') # Dealer will have money but not use it
        self.deck = deck
        
    def start(self):        
        """Begin the blackjack game."""
        self.deck.card_deck = Deck.shuffle(self.deck.card_deck)
        self.main_game_loop()


    def main_game_loop(self):
        """The method that will handle playing the game.
        The player will bet.
        The dealer will pass out cards.
        Check what the player wants to do.
        Dealer draws until 16+.
        Award money if applicable.
        Start the next hand if available.
        """
        bet = self.make_bet()
        self.deal_cards()
        player_hand_values = list(map(lambda x: x.value, self.player.hand))
        if (sum(player_hand_values) == 21):
            # We have a blackjack!
            # Check for a push
            self.blackjack_condition(bet)
        choice = self.get_player_choice()
        while True:
            if not self.handle_player_choice(choice): break
            player_hand_values = list(map(lambda x: x.value, self.player.hand))
            if (sum(player_hand_values) > 21): break            


    def handle_player_choice(self, choice: int):
        """Do something based on player choice.
        
        Parameter
        --------
        choice: int"""
        if choice == 1:
            self.deal_card(self.player)
            return True
        elif choice == 2:
            return False
        elif choice == 3:
            self.double_down()
            return True
        elif choice == 4:
            # Figure this out later.
            return True
        

    def double_down(self):
        """Get a new bet and continue"""



    def blackjack_condition(self, bet: int):
        """Handle what happens when your hand adds to 21
        
        Parameter
        --------
        bet: int - Initial bet"""
        dealer_hand_value = list(map(lambda x: x.value, self.dealer.hand))
        if (sum(dealer_hand_value) == 21):
            # Push
            self.player.push(bet)
        else:
            self.player.blackjack(bet)
        self.main_game_loop() # restart the game loop


    def get_player_choice(self) -> int:
        """Get the player choice for the current state.
        
        Returns
        -------
        int"""
        self.display_menu()
        return int(input('What will it be? '))


    def display_menu(self):
        """Show the menu with the avaialable options."""
        for key, item in PLAYER_CHOICES.items():
            if key != 4:
                print(f'{key}: {item}')
            else:
                if len(self.player.hand) == 2 and self.player.hand[0] == self.player.hand[1]:
                    print(f'{key}: {item}')

    
    def make_bet(self) -> int:
        """Method for handling making a bet.
        
        Returns
        ------
        int"""
        bet_amt = self.get_player_bet()
        self.player.place_bet(bet_amt)
        return bet_amt
    

    def get_player_bet(self) -> int:
        """Get a players bet.
        
        Returns
        ------
        int"""
        bet = int(input(f'Enter your bet (current balance: {self.player.money}): '))
        if bet > self.player.money:
            return self.player.money
        return bet
    

    def deal_cards(self):
        """Method for the first deal in the blackjack hand."""
        self.deck.deal_card(self.player)
        self.deck.deal_card(self.dealer)
        self.deck.deal_card(self.player)
        self.deck.deal_card(self.dealer)

    
    def deal_card(self, player: Player) -> None:
        """Method for when a player hits
        
        Parameter
        --------
        player: Player"""
        self.deck.deal_card(player)
