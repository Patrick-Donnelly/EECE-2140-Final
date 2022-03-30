# board.py by Patrick J. Donnelly
from tkinter import Tk, Frame
from .square import Square
from .pieces import *
from .logic.initialization import *

class Board:
    """An abstraction of a chessboard to hold Square() objects with TkInterface properties"""
    def __init__(self, master: Tk):
        """
        Creates the board
        :param master: The superior frame of the board; a Tk() objects
        """
        self.root = master
        self.frame = Frame(master)
        self.squares = [[[None] for _ in range(8)] for _ in range(8)]  # Standard 8x8 chessboard

        self.make_squares()
        self.frame.grid(row=0, column=0, rowspan=8, columnspan=8)

    def make_squares(self):
        """
        Creates all the Square() objects in the board
        """
        for i in range(8):
            for j in range(8):
                self.squares[i][j] = Square(self.frame, self, i, j, get_color(i, j), get_piece(i, j))
