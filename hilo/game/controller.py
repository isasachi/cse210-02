from game.card import Card

class Controller:

    def __init__(self):
        
        self.card = Card()
        self.choice = ""
        self.is_playing = True
        self.score = 300

    def start_game(self):
        
        while self.is_playing:
            self.show_card()
            self.update_game()
            self.play_again()

    def show_card(self):
        
        if not self.is_playing:
            return

        print(f"The card is: {self.card.value}")

    def update_game(self):

        if not self.is_playing:
            return

        self.choice = input("Higher or lower? [h/l] ")
        self.card.update_value()
        
        if self.card.hl_value == "e":
            self.score += 0

        if self.choice.lower() == self.card.hl_value:
            self.score += 100
        else:
            self.score -= 75

        print(f"Next card was: {self.card.value}")
        print(f"Your score is: {self.score}")

        if self.score == 0:
            self.is_playing = False

    def play_again(self):

        play_again = input("Play again? [y/n] ")
        if play_again.lower() == "y":
            self.is_playing = True
        else:
            self.is_playing = False
