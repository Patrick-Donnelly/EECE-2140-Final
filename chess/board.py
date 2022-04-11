# board.py by Patrick J. Donnelly
from tkinter import Frame
from .logic.board_logic import BoardLogic
from .square import Square

class Board:
    """An abstraction of a chessboard to hold Square() objects with TkInterface properties"""
    def __init__(self, master, container):
        """
        Creates the board
        :param master: The superior Frame() object of the board; a Tk() objects
        :param container: The superior GUI() object of the Board()
        """
        self.root = master
        self.frame = Frame(master)
        self.logic = BoardLogic(self, container)

        self.squares = [[None for _ in range(8)] for _ in range(8)]  # Standard 8x8 chessboard

        self.move = True  # The team of the current move; True if white, else False if black
        self.selected_square = None  # The current highlighted square on the board; by default is empty
        self.is_flipped = False  # States whether the board is inverted for aesthetic

        # Generate and update the frame of squares
        self.make_squares()
        self.frame.grid(row=0, column=0, rowspan=8, columnspan=8)

    # noinspection GrazieInspection
    def make_squares(self):
        """
        Creates all the Square() objects in the board
        """
        # Iterates through an 8x8 chessboard; Square.__init__() handles initialization
        for i in range(8):
            for j in range(8):
                # noinspection PyTypeChecker
                self.squares[i][j] = Square(self.frame, self, self.logic, i, j, i == 7, j == 0)

    def flip_board(self):
        """Flips and updates board"""
        self.is_flipped = not self.is_flipped
        self.update_squares()

    def reset_game(self):
        """Resets and updates game"""
        self.move = True
        self.is_flipped = False
        self.make_squares()
        # Doesn't require an update command because squares are destroyed and re-instantiated

    def set_view(self):
        """Changes perspective to the current player"""
        if self.move == self.is_flipped:
            self.flip_board()

    def update_squares(self):
        """Updates every square on the board"""
        for rank in self.squares:
            for square in rank:
                # noinspection PyUnresolvedReferences
                square.update()
