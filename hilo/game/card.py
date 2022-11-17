import random


class Card:
    """
    A small piece of cardboard with a number that could go from 1 to 13 written in one of its corners.

    Attributes:
        value (int): The number written in the card's corner.
        hl_value (string): The letter h, l or e.
    """

    def __init__(self):
        """Constructs a new instance of Card with a value and a hl_value attribute.

        Args:
            self (Card): An instance of Card.
        """

        self.value = random.randint(1, 13)
        self.hl_value = ""
    
    def update_value(self):
        """Randomly chooses a new card value, compares it with the previous value to determine if it's higher or lower and updates the previous value with the new value.

        Args:
            self (Card): An instance of Card.
        """

        new_value = random.randint(1, 13)
        if new_value > self.value:
            self.hl_value = "h"
        elif new_value < self.value:
            self.hl_value = "l"
        elif new_value == self.value:
            self.hl_value = "e"
        self.value = new_value