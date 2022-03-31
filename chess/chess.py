# chess.py by Patrick J. Donnelly
class Chess:
    """A wrapper class for the chess game"""
    def __init__(self):
        from .gui import GUI
        self.gui = GUI()

    def begin_game(self):
        self.gui.begin_game()
