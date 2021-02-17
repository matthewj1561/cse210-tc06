import time
class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """
    def __init__(self) -> None:
        self._answer = '99999'
        self._countdown = 4
 
    def read(self, prompt):
        """Gets text input from the user through the Console.

        Args: 
            self (Console): An instance of Console.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        self._answer = '99999'
        self._answer = input(prompt)
        return self._answer

    def read_for_turn(self):
        """Allows input for the player's guess

        Args: 
            self (Console): An instance of Console.
            

        Returns:
           str: user inputted answer
        """
        self._answer = '99999'
        self._answer = input()
        return self._answer
    
    def timer_for_turn(self):
        """Creates timed turns for game.
        Args:
            self: instance of Console
        Returns:
            str: answer that will never be true
        """
        time.sleep(self._countdown)

        if self._answer != '99999':
            return
        print("Gotta be faster than that!")
        self._answer = 'zzzz'
        return self._answer
        
        

    def read_number(self, prompt):
        """Gets numerical input from the user through the Console.

        Args: 
            self (Console): An instance of Console.
            prompt (string): The prompt to display to the user.

        Returns:
            integer: The user's input as an integer.
        """
        return int(input(prompt))
        
    def write(self, text):
        """Displays the given text on the Console. 

        Args: 
            self (Console): An instance of Console.
            text (string): The text to display.
        """
        print(text)
        