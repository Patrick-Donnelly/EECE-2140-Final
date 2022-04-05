# chess.py by Patrick J. Donnelly
from .gui import GUI

class Chess(GUI):
    """A wrapper class for the chess game; renamed for aesthetic"""
    def __init__(self):
        """Creates the GUI and, consequently, the chess game"""
        super().__init__()
