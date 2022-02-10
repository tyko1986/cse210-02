class Jumper:
    """A person who guesses letters to discover a word
    
    Responsibility: type his/her name and guess letters
    
    Attributes:
       jumper_name (string): the jumper's name
       wins (int): a number that shows if the jumper or the enquirer is the winner
       losses (int): a number that shows if the jumper or the enquirer is the loser
    """

    def __init__(self):
        """Constructs a new instance of Jumper
        
           self (Jumper): An instance of Jumper.
        """
        self.jumper_name = ""

    def get_jumper_name(self):
        """Asks for the Jumper's name
        """
        self.jumper_name = input("Please enter your name: ")
        return self.jumper_name
