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


    