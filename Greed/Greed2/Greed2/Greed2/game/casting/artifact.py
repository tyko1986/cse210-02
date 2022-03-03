from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. There are two kinds of artifacts, rocks ('#')  and gems ('$') 
    
    The responsibility of an Artifact is to add or rest points to the score

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message