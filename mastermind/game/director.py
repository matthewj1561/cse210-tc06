from game.roster import Roster
from game.player import Player
from game.console import Console
from game.board import Board
from game.logic import Logic

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
        self._console = Console()
        self._roster = Roster()
        self._logic = Logic()
        self.current_player = None

    
        
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
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
    
        Args:
        self (Director): An instance of Director.
        """
        
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            if n == 0:
                self.player1 = player
            else: 
                self.player2 = player
            self._roster.add_player(player)

        self._board = Board(self.player1, self.player2)

        board = self._board.create_board_string()
        self._console.write(board)
        self._logic.set_passcode()      
        print(self._logic.get_passcode())  
        

            
    


    def _get_input(self):
        """
        Asks the user input
        """
        self._roster.next_player()
        self.current_player = self._roster.get_current()
        self._console.write(f"{self.current_player.get_name()}'s turn:")
        self._player_guess = self._console.read("What is your guess? ")


        

    def _do_updates(self):
        """
        

        """
        if self._roster.current == 0:
            self.player1.set_guess(self._player_guess)
            

            player1_hint = self._logic.get_hint(self._logic.get_passcode(), self.player1.get_guess())
            self.player1.set_hint(player1_hint)
            print(self.player1.get_hint())

            board = self._board.update_board(self.player1.get_guess(),self.player1.get_hint(), self.player2.get_guess(), self.player2.get_hint() )
            self._console.write(board)

        elif self._roster.current == 1:
            self.player2.set_guess(self._player_guess)

            player2_hint = self._logic.get_hint(self._logic.get_passcode(), self.player2.get_guess())
            self.player2.set_hint(player2_hint)

            board = self._board.update_board(self.player1.get_guess(),self.player1.get_hint(), self.player2.get_guess(), self.player2.get_hint() )
            self._console.write(board)

        

        
        

        player = self._roster.get_current()
    
    def _do_output(self):

        ""
        print(self._logic.is_correct(self._player_guess))
        if self._logic.is_correct(self._player_guess) == True:
            self._console.write(f'{self.current_player} wins!')
            quit()
        elif self._logic.is_correct(self._player_guess) == False:
            pass