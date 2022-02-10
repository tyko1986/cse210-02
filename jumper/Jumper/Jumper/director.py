from enquirer import Enquirer
from jumper import Jumper

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
       enquirer (Enquirer): is the one who verifies if the letters given by the jumper are in the word
       jumper (Jumber): is the one who guesses the word
       result (string): is the result of who won and who lose the game
       continue_playing (boolean): the state of the game
       player_choice (string): the response of the Jumper after being asked
    """

    def __init__ (self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.enquirer = Enquirer()
        self.jumper = Jumper()
        self.result = ""
    
    def scenario (self):
        """Gives the welcome scenario to the user and starts the game. At the end, it shows the last scenario that will be
           winner message or loser message.

        Args:
           self (Director): an instance of Director
        """
        print("*********************************")
        print("***Welcome to Jumper Game***")
        print("*********************************")
        self.result = self.enquirer.start_game()
        self.end_game()

    def end_game(self):
        """Ends the game and displays wether the Jumper won or lose

        Args:
           self (Director): an instance of Director
        """
        if self.result == "W":
            self.msg_win()
        else:
            self.msg_lose()

    def msg_lose(self):
        print("\033[91mGosh, you've been hanged!\n")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           \33[0;0m \n")

    def msg_win(self):
        print("\033[93mCongratulations, You Won!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       \33[0;0m \n")