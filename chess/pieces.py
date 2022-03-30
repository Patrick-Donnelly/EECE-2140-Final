# pieces.py by Patrick J. Donnelly
class Piece:
    """The general template for all chessboard pieces"""
    # King = 0, Queen = 1, etc.
    LABELS = [['\u265A', '\u2654'], ['\u265B', '\u2655'], ['\u265C', '\u2656'],
              ['\u265D', '\u2657'], ['\u265E', '\u2658'], ['\u265F', '\u2659']]

    def __init__(self, team: bool):
        """
        Creates a general piece object
        :param team: The team of the piece: None, True (white), or False (black)
        """
        self.team = team
        self.label = None
        self.type = None
        self.set_label()

    def set_label(self):
        """
        Sets the label of the piece
        """
        if self.type is not None:
            self.label = self.LABELS[self.type][self.team]

class King(Piece):
    """An abstraction of a chess king"""
    def __init__(self, team: bool):
        super().__init__(team)
        self.type = 0

class Queen(Piece):
    """An abstraction of a chess queen"""

    def __init__(self, team: bool):
        super().__init__(team)
        self.type = 1

class Rook(Piece):
    """An abstraction of a chess rook"""

    def __init__(self, team: bool):
        super().__init__(team)
        self.type = 2

class Bishop(Piece):
    """An abstraction of a chess bishop"""
    def __init__(self, team: bool):
        super().__init__(team)
        self.type = 3

class Knight(Piece):
    """An abstraction of a chess knight"""
    def __init__(self, team: bool):
        super().__init__(team)
        self.type = 4

class Pawn(Piece):
    """An abstraction of a chess pawn"""
    def __init__(self, team: bool):
        super().__init__(team)
        self.type = 5
