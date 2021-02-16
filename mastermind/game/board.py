import random

class Board():
    """
    A board is the designated playing surface. The responsibility is to
    update the board based on the players guess and then create the
    string for the board.

    Stereotype:
        ???

    Attributes:
        pass

    """

    def __init__(self, player1, player2):
        """Class constructor. 

        Args:
            self (Board): An instance of the Board class.
        """
        self.player1_name = player1.get_name()
        

        self.player2_name = player2.get_name()

        self.board = []

    def update_board(self):
        """
        """
        pass

    def create_board_string(self):
        """
        """
         
        self.board =["---------------------\n",
                    f"{self.player1_name}: ----, ****\n",
                    f"{self.player2_name}: ----, ****\n",
                    "---------------------\n"]
        display_board = ''.join(self.board)
        return display_board

