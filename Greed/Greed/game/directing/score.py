class Score:
    """
    A value in points kept during the game.

    Class score keeps track of how many points the player is earning or loosing.

    Attributes:

    myScore(int): The actual total points
    """


    def __init__(self):
        self.myScore = 0
        pass

    def set_score_plus(self):
        self.myScore = self.myScore + 1
        
        pass

    def set_score_minus(self):
        self.myScore = self.myScore - 1
        
        pass 

    def get_score(self):
        return self.myScore