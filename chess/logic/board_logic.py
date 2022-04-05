# board_logic.py by Patrick J. Donnelly
from .move_logic import MoveLogic
from .legality_logic import LegalityLogic

class BoardLogic:
    """Represents the board-level logic of the program"""
    def __init__(self, board, gui):
        self.board = board
        self.gui = gui
        self.move_logic = MoveLogic(self)
        self.legality_logic = LegalityLogic(self.move_logic)

    def abort_move(self):
        """
        Resets the board to a selection state
        """
        self.board.selected_square = None
        self.remove_highlights()

    def has_legal_moves(self) -> bool:
        """
        Determines whether a given piece has legal moves
        :return: A Boolean representing whether a given piece has legal moves
        """
        for rank in self.board.squares:
            for square in rank:
                if self.legality_logic.is_legal(square):
                    return True
        return False

    def highlight_legal_moves(self):
        """
        Highlights all the legal spaces available to the selected piece
        """
        self.board.selected_square.is_inverted = True
        self.board.selected_square.update()

        for rank in self.board.squares:
            for square in rank:
                if self.legality_logic.is_legal(square):
                    square.is_inverted = True
                    square.update()

    def remove_highlights(self):
        """
        Removes any highlighting from all squares on the board
        """
        for rank in self.board.squares:
            for square in rank:
                if square.is_inverted:
                    square.is_inverted = False
                    square.update()
