from classes.card import Card


class Player:
    """Player class for keeping track of player money and such."""

    def __init__(self, name: str, money: int = 1000):
        """Constructor

        Parameters
        ---------
        name: str - The player's name
        money: int - The amount of money the player can bet with"""
        self.name = name
        self.money = money
        self.hand: list[Card] = []

    def place_bet(self, amount: int) -> None:
        """Subtract the amount from the player's current holdings.

        Parameter
        ---------
        amount: int"""
        self.money -= amount

    def push(self, amount: int) -> None:
        """In the event of a push, just add the money back.

        Parameter
        --------
        amount: int"""
        self.money += amount

    def win(self, amount: int) -> None:
        """In the event of a win, increase the amount by 2 and then add it to money"""
        self.money += amount + amount

    def blackjack(self, amount: int) -> None:
        """In the event of blackjack, increase the amount by 2.5 and then add it to money."""
        self.money += int(amount + amount + (amount / 2))

    def get_hand_value(self) -> int:
        """Return the current hand value of the player

        Returns
        ------
        int"""
        values = list(map(lambda x: x.value, self.hand))
        return sum(values)
