# board.py by Patrick J. Donnelly
from tkinter import Frame
from .logic.board_logic import BoardLogic
from .square import Square

class Board:
    """An abstraction of a chessboard to hold Square() objects with TkInterface properties"""
    def __init__(self, master):
        """
        Creates the board
        :param master: The superior frame of the board; a Tk() objects
        """
        self.root = master
        self.frame = Frame(master)
        self.logic = BoardLogic(self)
        self.squares = [[[None] for _ in range(8)] for _ in range(8)]  # Standard 8x8 chessboard
        self.move = True  # True: white, False: black; white begins
        self.selected_square = None
        self.is_flipped = False

        self.make_squares()
        self.frame.grid(row=0, column=0, rowspan=8, columnspan=8)

    def make_squares(self):
        """
        Creates all the Square() objects in the board
        """
        for i in range(8):
            for j in range(8):
                self.squares[i][j] = Square(self.frame, self, self.logic.move_logic, i, j, i == 7, j == 0)

    def flip_board(self):
        self.is_flipped = not self.is_flipped
        self.update_squares()

    def reset_game(self):
        self.move = True
        self.is_flipped = False
        self.make_squares()
        # Doesn't require an update command because squares are destroyed and re-instantiated

    def set_view(self):
        if self.move == self.is_flipped:
            self.flip_board()

    def update_squares(self):
        for rank in self.squares:
            for square in rank:
                square.update()
