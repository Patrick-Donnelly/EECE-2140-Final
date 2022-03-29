# gui.py by Patrick J. Donnelly
from tkinter import *
from board import Board

class GUI:
    """The beating heart of the chess program; handles TkInterface objects"""
    def __init__(self):
        self.root = Tk()
        self.root.title("Chess")
        self.root.geometry('640x720')

        self.board = Board(self.root)

    def begin_game(self):
        self.root.mainloop()
