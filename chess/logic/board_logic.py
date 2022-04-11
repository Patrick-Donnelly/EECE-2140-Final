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

    def master_button_action(self, square):
        """
        Sice Tkinter buttons can only have one command, this function serves as that command
        :param square: The square attached to the button
        """
        # If there is a highlighted square, either attempt or abort capture
        # If you attempt to highlight an enemy or null piece, nothing happens
        if square.container.selected_square:
            # If the selected square is the given square, abort capture
            if square.container.selected_square is square:
                self.abort_move()
            else:
                # If the pieces are on opposite teams, attempt capture; else, abort
                if square.piece.team != square.container.move:
                    self.move_logic.attempt_capture(square)
                else:
                    self.abort_move()
        elif square.piece.team == square.container.move:
            square.container.selected_square = square
            if self.has_legal_moves():
                self.highlight_legal_moves()
            else:
                self.abort_move()

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
        self.board.selected_square.is_highlighted = True
        self.board.selected_square.update()

        for rank in self.board.squares:
            for square in rank:
                if self.legality_logic.is_legal(square):
                    square.is_highlighted = True
                    square.update()

    def remove_highlights(self):
        """
        Removes any highlighting from all squares on the board
        """
        for rank in self.board.squares:
            for square in rank:
                if square.is_highlighted:
                    square.is_highlighted = False
                    square.update()
