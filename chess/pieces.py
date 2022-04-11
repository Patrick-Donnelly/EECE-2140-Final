# pieces.py by Patrick J. Donnelly
class Piece:
    """The general template for all chessboard pieces"""
    # Unicode values for chess piece emojis. I do not have the patience for art.
    # King = 0, Queen = 1, etc.
    LABELS = [['\u265A', '\u2654'], ['\u265B', '\u2655'], ['\u265C', '\u2656'],
              ['\u265D', '\u2657'], ['\u265E', '\u2658'], ['\u265F', '\u2659']]

    def __init__(self, team: bool or None):
        """
        Creates a general piece object
        :param team: The team of the piece: None, True (white), or False (black)
        """
        self.team = team
        self.label = ' '  # The image associated with the piece
        self.type = None  # The type of the piece for internal use
        self.has_moved = False  # Used for pawn moves, castling, and en passant

    def set_label(self):
        """
        Sets the label of the piece
        """
        if self.type is not None:
            self.label = self.LABELS[self.type][self.team]

    def __bool__(self):
        """
        Defines the Boolean interpretation of the piece, specifically for null pieces
        :return: A Boolean corresponding to whether the piece is not null
        """
        return self.team is not None

    def __str__(self):
        """
        Defines the string of a given piece
        :return: A string representing the piece
        """
        return self.label

class King(Piece):
    """An abstraction of a chess king"""
    def __init__(self, team: bool):
        super().__init__(team)
        self.type = 0
        self.set_label()

class Queen(Piece):
    """An abstraction of a chess queen"""
    def __init__(self, team: bool):
        super().__init__(team)
        self.type = 1
        self.set_label()

class Rook(Piece):
    """An abstraction of a chess rook"""
    def __init__(self, team: bool):
        super().__init__(team)
        self.type = 2
        self.set_label()

class Bishop(Piece):
    """An abstraction of a chess bishop"""
    def __init__(self, team: bool):
        super().__init__(team)
        self.type = 3
        self.set_label()

class Knight(Piece):
    """An abstraction of a chess knight"""
    def __init__(self, team: bool):
        super().__init__(team)
        self.type = 4
        self.set_label()

class Pawn(Piece):
    """An abstraction of a chess pawn"""
    def __init__(self, team: bool):
        super().__init__(team)
        self.type = 5
        self.set_label()
