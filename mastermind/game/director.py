from game.roster import Roster
from game.player import Player
from game.console import Console
from game.board import Board
from game.logic import Logic
from threading import Thread
import time

class Director:
    """
    A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        _console = An instance of the Console class
        _logic = An instance of the Logic class
        _roster = An instance of the Roseter class
        _keep_playing (boolean) = Defines whether or not the game loop should continue
        _player_guess (string) = Holds the most recent player's guess
        _passcode (string) = The code the players are trying to guess. Since this is a static attribute, 
                             it is convient to define it here and use it throughout the program instead of 
                             calling the on the _logic class every time. 
    """
    def __init__(self):

        self._passcode = ''
        self._player_guess = ''
        self._keep_playing = True
        self._console = Console()
        self._roster = Roster()
        self._logic = Logic()
        
    def start_game(self):
        """
        Starts the game loop
        """

        self._prepare_game()
        while self._keep_playing == True:
            self._get_input()
            self._do_updates()
            self._do_output()

    def _prepare_game(self):
        """Prepares the game before it begins. 
           This entails :
                Adding each play to the board
                Creating and displaying the intial board
                Setting the passcode

        Args:
        self (Director): An instance of Director.
        """

        # A simple loop to identify each player and add them to the roster
        self._console.write("Welcome to the H.A.C.K.")
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            if n == 0:
                self.player1 = player
            else: 
                self.player2 = player
            self._roster.add_player(player)

        # Creates the board class with the two new players
        self._board = Board(self.player1, self.player2)

        #Creates the first board and displays it to the terminal 
        board = self._board.create_board_string()
        self._console.write(board)

        #Uses the logic class to set the passcode that will be used for the game
        self._logic.set_passcode()      

    def _get_input(self):
        """
        Asks the user for their guess each round, also switches the turns before any further actions
        """
        #Begins the turn system
        self._roster.next_player()

        #Retrieves and displays whoever's turn it is
        self.current_player = self._roster.get_current()
        self._console.write(f"{self.current_player.get_name()}'s guess:")
        Thread(target = self._console.timer_for_turn).start()
        Thread(target = self._console.read_for_turn).start()
        time.sleep(self._console._countdown)
        
        self._player_guess = self._console._answer
    def _do_updates(self):
        """
        An in depth "if" statement that updates key game information based on the user's input and current player

        """
        # If the player is number 1, then the board is updated according to what they entered. The same is true for player 2.
        if self._roster.current == 0:

            self.player1.set_guess(self._player_guess)
            

            player1_hint = self._logic.get_hint(self._logic.get_passcode(), self.player1.get_guess())
            self.player1.set_hint(player1_hint)

            board = self._board.update_board(self.player1.get_guess(),self.player1.get_hint(), self.player2.get_guess(), self.player2.get_hint() )
            self._console.write(board)

        elif self._roster.current == 1:

            self.player2.set_guess(self._player_guess)

            player2_hint = self._logic.get_hint(self._logic.get_passcode(), self.player2.get_guess())
            self.player2.set_hint(player2_hint)

            board = self._board.update_board(self.player1.get_guess(),self.player1.get_hint(), self.player2.get_guess(), self.player2.get_hint() )
            self._console.write(board)

    
    def _do_output(self):
        """
        Determines if the game will continue or end
        """

        if self._logic.is_correct(self._player_guess) == True:
            self._console.write(f'{self._roster.get_current().get_name()} Wins!!')
            self._console.write("""
___________________ __________    _____________________________________________________________
\__    ___/\_____  \ ______   \  /   _____/\_   _____/\_   ___ \______   \_   _____/\__    ___/
  |    |    /   |   \|     ___/  \_____  \  |    __)_ /    \  \/|       _/|    __)_   |    |   
  |    |   /    |    \    |      /        \ |        \|     \___|    |   \|        \  |    |   
  |____|   \_______  /____|     /_______  //_______  / \______  /____|_  /_______  /  |____|   
                   \/                   \/         \/         \/       \/        \/            
   _____ _____________________   _____     .____________                                       
  /  _  \ |_____   \_   _____/  /  _  \    |   ____/_   |                                      
 /  /_\  \|       _/|    __)_  /  /_\  \   |____  \ |   |                                      
/    |    \    |   \|        \/    |    \  /       \|   |                                      
\____|__  /____|_  /_______  /\____|__  / /______  /|___|                                      
        \/       \/        \/         \/         \/                   
            You're in...""")
            self._keep_playing = False
        
        elif self._logic.is_correct(self._player_guess) == False:
            self._keep_playing == True
