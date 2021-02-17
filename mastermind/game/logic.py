import random as rand

class Logic():

    
    def __init__(self) -> None:
        """
        Initializes the class. 
        __passcode = key that the game is based on 
        __hint = string that is returned for a guess
        """
        self.__passcode = ''
        self.__hint = ""
        self.__win = False
   
    def get_hint(self, code, guess):
        """
        Returns a hint to the user

        Inputs: self, instance of a logic class
                guess, 4 letter numeric string
        """ 
        error = "INVALID GUESS YOU SWINE"
        number_check = guess.isnumeric()
        # debugging
        # print(f'In Logic.get_hint(), code = {code}, type = {type(code)}')
        # print(f'In Logic.get_hint(), guess = {guess}, type = {type(guess)}')

        if len(guess) != 4:
            return error
        elif number_check is False:
            return error
        else:
            hint = ""
            for index, letter in enumerate(guess):
                if code[index] == letter:
                    hint += "x"
                elif letter in code:
                    hint += "o"
                else:
                    hint += "*"
            return hint
    
    def set_passcode(self):
        """
        Sets a new passcode and assigns it to the passcode attribute
        """
        list_passcode = []
        
        for i in range(4):
            number = rand.randint(0,9)
            list_passcode.append(str(number))
        # Debugging
        # print(f'In Logic.set_passcode(), list_passcode = {list_passcode}, type = {type(list_passcode)}')


        for elm in list_passcode:
            self.__passcode += elm
            # debugging
            # print(f'In Logic.set_passcode(), elm = {elm}')
        # print(f'In Logic.set_passcode(), self.__passcode = {self.__passcode}, type = {type(self.__passcode)}')

    def get_passcode(self):
        """
        Returns the passcode.
        """
        return self.__passcode

    def is_correct(self, guess):
        """
        Returns: Boolean
            True if the guess matches the passcode
            False if the guess does not match
        """
        number_check = guess.isnumeric()

        if len(guess) != 4:
            return False
        elif number_check is False:
            return False
        
        if guess == self.__passcode:
            return True
        else:
            return False
