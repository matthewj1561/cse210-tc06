class Player:
    """A person taking part in a game. The responsibility of Player is to keep track of their identity and last move.
    
    Stereotype: 
        Information Holder

    Attributes:
        _name (string): The player's name.
        _move (Move): The player's last move.
    """
    def __init__(self, name):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self._name = name
        self._guess = None
        self._hint = None
        
    def get_name(self):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        return self._name

    def get_guess(self):
        """Returns the player's last guess. If the player 
        hasn't guessed yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        return self._guess    

    def set_guess(self, guess):
        """Sets the player's last guess to the given argument guess.

        Args:
            self (Player): an instance of Player.
            guess: a four char string for the player's guess.
        """
        self._guess = guess

    def get_hint(self):
        """Returns the player's most recent hint.

        Args:
            self (Player): an instance of Player.
        """
        return self._hint

    def set_hint(self, hint):
        """Set's the player's hint to the given argument.

        Args:
            self (Player): an instance of Player.
            hint: a four char string for the hint
        """
        self._hint = hint
