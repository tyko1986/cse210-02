from player import Player
from random_number import Number

class Dealer:
    """It's a person who leads the game.
    
    The responsibility of a Dealer is to show the cards, ask 
    the player if he/she wants to continue playing, and output
    the results.
    
    Attributes:
        name: a string. The Player's name
        user_choice: a string. It can be "l"(lower) or "h"(higher)
        first_number: a string. The value of the showed card
        second_number: a string. The value of the next card
        score: an integer. The player's score. It starts with 300
        quit: a "y"(yes) character. If the player inputs this, the game is over
        game_over : a string. The messege that players will see when the game is over
    """
    
    def __init__(self):
        """Constructs a new Dealer
        """
        self.name = ""
        self.user_choice = ""
        self.first_number = ""
        self.second_number = ""
        self.score = 300
        self.random_result = ""
        self.quit = "y"
        self.game_over = ""
        pass

    def game(self):
        """Calls the other functions and attributes in order
        """
        self.name = Player.name()
        print(f"\nHi {self.name}... WELCOME!!!")
        print(f"Your current score is: {self.score}")
        while self.score > 0 and self.quit.lower() == "y":
            self.first_number = Number.sorted_number()
            self.second_number = Number.sorted_number()
            print("The card is: ", self.first_number)
            Dealer.users_choice(self)
            print("Next card was: ", self.second_number)
            Dealer.compare_numbers(self)
            Dealer.compare_user_choice(self)
            print("Your score is: ", self.score)
            if self.score > 0 and self.quit.lower() == "y":
                self.quit = input("Play again? y or n   ")
                while self.quit.lower() != "y" and self.quit.lower() != "n":
                     self.quit = input("Please, Play again? y or n   ")
            print("")
        print(self.game_over)
    pass


    def users_choice(self):
        """Asks the user to choose an option and validate his/her input
        """
        self.user_choice = input("Higher or Lower [h / l]: ")
        while self.user_choice.lower() != "h" and self.user_choice.lower() != "l":
            self.user_choice = input("Please, type Higher or Lower [h / l]: ")
        pass

    def compare_numbers(self):
        """Calculates the result
        """
        if self.first_number < self.second_number:
            self.random_result = "h"
        else:
            self.random_result = "l"

    def compare_user_choice(self):
        """Compares the player's choice to the result
        """
        if self.user_choice.lower() == self.random_result:
            self.score += 100
        else:
            self.score -= 75

        if self.score <= 0:
            self.game_over = "GAME OVER"
        pass
        
