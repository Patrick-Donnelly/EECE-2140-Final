# square.py by Patrick J. Donnelly
from tkinter import Frame
from .pieces import Piece

class Square:
    """An abstraction of a chessboard square to hold Piece() objects with TkInterface properties"""
    # Hex colors for black and white squares
    WHITE_SQUARE = '#bfbfbf'
    BLACK_SQUARE = '#994d00'

    def __init__(self, master: Frame, rank: int, file: int, piece: Piece, rank_label=None, file_label=None):
        self.master = master
        self.rank = rank
        self.file = file
        self.color = self.get_color(rank, file)
        self.piece = piece
        self.rank_label = rank_label
        self.file_label = file_label
        self.square = None

        self.set_square()

    def get_color(self, rank: int, file: int) -> str:
        """
        A simple formula for determining the appropriate color for the square
        :param rank: The rank (row) of the square
        :param file: The file (column) of the square
        :return: A string corresponding to the appropriate background color of the square
        """
        # Using taxicab distance, determine proper color
        if (rank + file) % 2 == 0:
            return self.WHITE_SQUARE
        else:
            return self.BLACK_SQUARE

    def set_square(self):
        """
        Set the properties of the square, taking into account rank and file labels
        """
        self.square = Frame(self.master, bg=self.color, width=80, height=80)
        self.square.grid(row=self.rank, column=self.file)
