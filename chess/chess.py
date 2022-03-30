# chess.py by Patrick J. Donnelly
from .gui import GUI

class Chess:
    """A wrapper class for the chess game"""
    def __init__(self):
        self.gui = GUI()

    def begin_game(self):
        self.gui.begin_game()
