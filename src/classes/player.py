class Player:
    """Player class for keeping track of player money and such."""
    def __init__(self, name: str, money: int) -> None:
        """Constructor
        
        Parameters
        ---------
        name: str - The player's name
        money: int - The amount of money the player can bet with"""
        self.name = name
        self.money = money


    