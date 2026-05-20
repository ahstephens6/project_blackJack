from classes.player import Player
from classes.deck import Deck

from utils.constants import PLAYER_CHOICES, DEALER_LIMIT, BUST


class Game:
    """Class for handling gamestate"""

    def __init__(self, player: Player, deck: Deck):
        """Constructor

        Parameters
        ---------
        player: Player - The player for the blackjack game
        deck: Deck - The deck for the blackjack game"""
        self.player = player
        self.dealer = Player('Dealer')  # Dealer will have money but not use it
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
        Dealer draws until DEALER_LIMIT+.
        Award money if applicable.
        Start the next hand if available.
        """
        play_again_condition = ['y', 'yes', 'Yes', 'Y', 'True']
        play_again = 'y'
        while play_again in play_again_condition:
            bet = self.make_bet()
            self.deal_cards()
            if (self.player.get_hand_value() == BUST):
                self.blackjack_condition(bet)

            choice = self.get_player_choice()
            while True:
                to_continue, double_down = self.handle_player_choice(choice)
                if double_down:
                    bet += double_down
                if not to_continue:
                    break
                if (self.player.get_hand_value() > BUST):
                    break
                choice = self.get_player_choice(double_down=False)

            if self.player.get_hand_value() > BUST:
                self.player_loses()
            while self.dealer.get_hand_value() < DEALER_LIMIT:
                self.deal_card(self.dealer)
            if (self.dealer.get_hand_value() > BUST) or (self.player.get_hand_value() > self.dealer.get_hand_value()):
                self.player_win()

            play_again = input('Another hand (y/n)? ')

    def player_win(self):
        """Handle the win state for the player."""

    def player_loses(self):
        """Handle the lose state for the player."""

    def handle_player_choice(self, choice: int) -> tuple[bool, int | None]:
        """Do something based on player choice.

        Parameter
        --------
        choice: int

        Returns
        -------
        tuple[bool, int | None]"""
        if choice == 1:
            # Hit
            self.deal_card(self.player)
            return True, None
        elif choice == 2:
            # Stand
            return False, None
        elif choice == 3:
            # Double Down
            bet: int = self.double_down()
            return False, bet
        elif choice == 4:
            # Split
            # Figure this out later.
            return True, None
        return False, None

    def double_down(self) -> int:
        """Get a new bet and continue

        Returns
        ------
        int"""
        return self.make_bet(double_down=True)

    def blackjack_condition(self, bet: int):
        """Handle what happens when your hand adds to 21

        Parameter
        --------
        bet: int - Initial bet"""
        if self.dealer.get_hand_value() == BUST:
            # Push
            self.player.push(bet)
        else:
            self.player.blackjack(bet)
        self.main_game_loop()  # restart the game loop

    def get_player_choice(self, double_down: bool = True) -> int:
        """Get the player choice for the current state.

        Parameter
        --------
        double_down: bool - if double down should be displayed.

        Returns
        -------
        int"""
        self.display_menu(double_down)
        return int(input('What will it be? '))

    def display_menu(self, double_down: bool):
        """Show the menu with the avaialable options.

        Parameter
        --------
        double_down: bool"""
        for key, item in PLAYER_CHOICES.items():
            if key == 3 and double_down:
                print(f'{key}: {item}')
            elif key == 4:
                if len(self.player.hand) == 2 and self.player.hand[0] == self.player.hand[1]:
                    print(f'{key}: {item}')
            else:
                print(f'{key}: {item}')

    def make_bet(self, double_down: bool = False) -> int:
        """Method for handling making a bet.

        Parameter
        --------
        double_down: bool - If the player is doubling down

        Returns
        ------
        int"""
        bet_amt = self.get_player_bet(double_down)
        self.player.place_bet(bet_amt)
        return bet_amt

    def get_player_bet(self, double_down: bool = False) -> int:
        """Get a players bet.

        Parameter
        --------
        double_down: bool - condition to change prompt

        Returns
        ------
        int"""
        bet = 0
        if double_down:
            bet = int(
                input(f'Double down bet (current balance: {self.player.money}): '))
        else:
            bet = int(
                input(f'Enter your bet (current balance: {self.player.money}): '))
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
