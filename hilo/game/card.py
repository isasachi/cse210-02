import random


class Card:

    def __init__(self):
        
        self.value = random.randint(1, 13)
        self.hl_value = ""
    
    def update_value(self):

        new_value = random.randint(1, 13)
        if new_value > self.value:
            self.hl_value = "h"
        elif new_value < self.value:
            self.hl_value = "l"
        elif new_value == self.value:
            self.hl_value = "e"
        self.value = new_value