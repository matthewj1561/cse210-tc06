import random as rand

class Logic():

    """
    Initializes the class. 
    __passcode = key that the game is based on 
    __hint = string that is returned for a guess
    """
    def __init__(self) -> None:
        self.__passcode = []
        self.__hint = ""
        self.__win = False

    """
    Returns a hint to the user

    Inputs: self, instance of a logic class
            guess, 4 letter numeric string
    """    
    def get_hint(self, guess):
        error = "INVALID GUESS YOU SWINE"
        number_check = guess.isnumeric()

        if len(guess) != 4:
            return error
        elif number_check is False:
            return error
        else:
            return self.__hint
    """
    Sets a new passcode and assigns it to the passcode attribute
    """
    def set_passcode(self):
        self.__passcode = []

        for i in range(4):
            number = rand.randint(0,9)
            self.__passcode.append(number)
        

    def get_passcode(self):
        return self.__passcode

    def is_correct(self, guess):
        number_check = guess.isnumeric()

        if len(guess) != 4:
            return False
        elif number_check is False:
            return False
        
        if self.__passcode == guess:
            pass

test = Logic()

test.set_passcode()
print(test.get_passcode())