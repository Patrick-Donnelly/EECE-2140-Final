# board.py by Patrick J. Donnelly
from tkinter import Tk, Frame
from .square import Square
from .pieces import *

class Board:
    """An abstraction of a chessboard to hold Square() objects with TkInterface properties"""
    WHITE_SQUARE = '#bfbfbf'
    BLACK_SQUARE = '#994d00'

    def __init__(self, master: Tk):
        """
        Creates the board
        :param master: The superior frame of the board; a Tk() objects
        """
        self.root = master
        self.frame = Frame(master)
        self.squares = [[[None] for _ in range(8)] for _ in range(8)]  # Standard 8x8 chessboard

        self.make_squares()
        self.place_squares()

    def make_squares(self):
        """
        Creates all the Square() objects in the board
        """
        for i in range(8):
            for j in range(8):
                self.squares[i][j] = Square(i, j, self.get_color(i, j), self.get_piece(i, j))

    def get_color(self, rank: int, file: int) -> str:
        # Using taxicab distance, determine proper color
        if rank + file % 2 == 0:
            return self.WHITE_SQUARE
        else:
            return self.BLACK_SQUARE

    def get_piece(self, rank: int, file: int) -> Piece:
        pass

    def place_squares(self):
        pass

