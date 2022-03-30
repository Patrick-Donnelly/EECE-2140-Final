# square.py by Patrick J. Donnelly
from tkinter import Frame, Button
from .pieces import *

class Square:
    """An abstraction of a chessboard square to hold Piece() objects with TkInterface properties"""

    def __init__(self, master: Frame, container, rank: int, file: int,
                 color: str, piece: Piece, rank_label=None, file_label=None):
        self.master = master
        self.container = container
        self.rank = rank
        self.file = file
        self.color = color
        self.piece = piece
        self.rank_label = rank_label
        self.file_label = file_label
        self.square = None

        self.set_square()

    def set_square(self):
        """
        Set the properties of the square, taking into account rank and file labels
        """
        # Delete the active frame if applicable
        if self.square:
            self.square.destroy()

        # Create the frame according to the class parameters
        self.square = Frame(self.master, bg=self.color, width=80, height=80)
        self.square.grid(row=self.rank, column=self.file)

        # Place a button over top of the frame
        Button(self.square, bg=self.color, text=self.piece.label).pack(fill='both')

