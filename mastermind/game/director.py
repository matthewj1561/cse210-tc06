from game.roster import Roster
from game.player import Player
from game.console import Console
from game.board import Board
# from game.logic import Logic

class Director:
    """
    A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        

    General Workflow:

    """
    def __init__(self):

        self._passcode = ''
        self._player_guess = ''
        self._keep_playing = True
        _console = Console()
        _roster = Roster()
        _board = Board()
        _logic = Logic()

    
        
    def start_game(self):
        """
        Starts the game loop
        """

        _prepare_game()
        while self.keep_playing:
            self.get_input
            self.do_updates
            self.do_output

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
    
        Args:
        self (Director): An instance of Director.
        """
    
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
    


    def _get_input(self):
        """
        Asks the user input
        """
        board = self._board.to_string()
        self._console.write(board)
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        player_guess = self._console.read("What is your guess? ")


        

    def _do_updates(self):
        """
        

        """
        #TODO
        player = self._roster.get_current()
    
    def _do_output(self):

        ""
        if _logic.is_correct() == True:
            pass
        elif _logic.is_correct() == False:
            self._keep_playing == False