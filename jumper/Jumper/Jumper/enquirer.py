from dictionary import Dictionary
from jumper import Jumper
class Enquirer:
    """A person who lets the Jumper know if the letter that he or she said is part of the word.
    
    Responsibility: compare the letter said by the Jumper and let him or her know if it is correct.
    
    Attributes:
        word (string): the jumper must find out
        letter (srting): a string that represents each letter of the word
        parachute (int): the amount of attempts that the jumper has
        guessed_letters (string): the letters already guessed by the jumper
        missing_letters (string): the letters that the jumper is missing
        guess (string): an attempt from the jumper
        error (int): the amoint of errors the jumper is acumulating
        finish (string): the result of Jumper (if he/she won or lose)
        name: the user name
    """

    def __init__(self):
        """Constructs a new instance of Enquirer
        
           self (Enquirer): An instance of Enquirer.
        """        
        self.word = ""
        self.letter = ""
        self.parachute_points = 5
        
        self.guessed_letters = []
        self.missing_letters = ""
        self.guess = ""
        self.error = 0
        self.keep_playing = True
        self.finish = ""     # W = wins     L = lose
        self.name = ""


    def request_letter(self):
        """Asks the jumper for a letter
        
        Args:
           self (Enquirer): an instance of Enquiror
        """
        self.guess = input("\nType a letter ")
        self.guess = self.guess.strip().lower()
        return self.guess

    def letters_length(self):
        """Displays the amount of letters, showing a "_" symbol for each letter

        Args:
           self (Enquirer): and instance of Enquiror
        """
        return ["_" for self.letter in self.word]

    def compare_letters(self):
        """Compares the letter guessed by the jumper to the letters of the word

        Args:
           self (Enquirer): and instance of Enquiror
        """
        self.guessed_letters = self.letters_length(self.word)

        
    def mark_right_guess(self):
        """Replaces the underscore symbol with the right letter

        Args:
           self (Enquirer): and instance of Enquiror
        """
        index = 0
        no_letter=0
        for self.letter in self.word:
            if (self.guess == self.letter):
                self.guessed_letters[index] = self.letter
                no_letter = 1
            index += 1
        if no_letter == 0:
            self.error += 1

    def start_game(self):
        """Starts the game with the functions declared before

        Args:
           self (Enquirer): and instance of Enquiror
        """
        word = Dictionary()
        player = Jumper()
        self.name = player.get_jumper_name()
        self.word = word.words()
        self.letters = self.letters_length()
        self.guessed_letters = self.letters_length()
        print(f"Good luck for you {self.name}!!!")
        self.parachute()
        print(f"\n", self.letters_length())
        while self.keep_playing:
            self.request_letter()
            self.mark_right_guess()
            self.check_match()
        return self.finish

    def check_match(self):
        """Checks the state of the game; how many attempts does the jumper have left

        Args:
           self (Enquirer): and instance of Enquiror
        """
        self.missing_letters = self.guessed_letters.count('_')
        if(self.missing_letters) == 0:
            print(f"\nCongratulations!! You guessed the secret word: {self.word.upper()}")
            self.keep_playing = False
            self.finish = "W"
        else:
            print("")
            print(self.guessed_letters)
            print('\nYou still need to guess {} letter(s)'.format(self.missing_letters))
            print('You still have {} tries'.format(5-self.error))
            self.parachute()
            if self.error == 5:
                self.keep_playing = False
                self.finish = "L"
                print(f"\nThe secret word is: {self.word.upper()}")
        pass


    def parachute(self):
        """Displays a figure of a man with a parachutes
        """
        if self.error == 0:
            print("")
            print(" ___ ")
            print("/___\ ")
            print("\   /")
            print(" \ /")
            print("  0")
            print(" /|\ ")
            print(" / \ ")
        elif self.error == 1:
            print("")
            print("/___\ ")
            print("\   /")
            print(" \ /")
            print("  0")
            print(" /|\ ")
            print(" / \ ")
        elif self.error == 2:
            print("")
            print("\   /")
            print(" \ /")
            print("  0")
            print(" /|\ ")
            print(" / \ ")
        elif self.error == 3:
            print("")
            print(" \ /")
            print("  0")
            print(" /|\ ")
            print(" / \ ")
        elif self.error == 4:
            print("")
            print("  0")
            print(" /|\ ")
            print(" / \ ")
        elif self.error == 5:
            print("")
            print("  x")
            print(" /|\ ")
            print(" / \ ")
        pass

    def guesses(self):

        pass

