from game.card import Card

class Controller:
    """
    The Controller is responsible of controlling the sequence of play.

    Attributes:
        card (Card): A Card instance.
        choice (string): The higher or lower choice of the player.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
    """

    def __init__(self):
        """Constructs a new Controller.
        
        Args:
            self (Controller): an instance of Controller.
        """

        self.card = Card()
        self.choice = ""
        self.is_playing = True
        self.score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Controller): an instance of Controller.
        """
        
        while self.is_playing:
            self.show_card()
            self.update_game()
            self.play_again()

    def show_card(self):
        """Shows the initial card value.
        
        Args:
            self (Controller): an instance of Controller.
        """

        if not self.is_playing:
            return

        print(f"The card is: {self.card.value}")

    def update_game(self):
        """Asks the player to choose higher or lower, then updates the card's value and the player's score.
        
        Args:
            self (Controller): an instance of Controller.
        """

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
        """Asks the player if he wants to start a new round.
        
        Args:
            self (Controller): an instance of Controller.
        """

        play_again = input("Play again? [y/n] ")
        if play_again.lower() == "y":
            self.is_playing = True
        else:
            self.is_playing = False
