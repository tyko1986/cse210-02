import random
class Dictionary:
    """Stores a list of words from which randomly returns one
    
       The responsibility is to provide a random word
       
       Attributes: 
    """
    
    def __init__(self):
        """Constructs a new instance of Dictionary
        
           self (Dictionary): An instance of Dictionary.
        """
        self.list = ["monkey", "lion", "fish", "horse", "serpent", "falcon", "alligator", "armadillo", "butterfly", 
        "chameleon", "elephant", "giraffe"]

    def words(self):
        """Returns a random word from the list

        Arguments: 
            self (Dictionary): an instance of Dictionary 
        """
        return random.choice(self.list)