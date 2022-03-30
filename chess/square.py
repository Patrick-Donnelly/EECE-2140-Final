# square.py by Patrick J. Donnelly
from tkinter import Frame
from .pieces import Piece

class Square:
    """An abstraction of a chessboard square to hold Piece() objects with TkInterface properties"""
    def __init__(self, master: Frame, rank: int, file: int, color: str, piece: Piece, rank_label=None, file_label=None):
        self.master = master
        self.rank = rank
        self.file = file
        self.color = color
        self.piece = piece
        self.square = None

        self.set_square()

    def set_square(self):
        self.square = Frame(self.master, bg=self.color, width=80, height=80)
        self.square.grid(row=self.rank, column=self.file)
