# move_logic.py by Patrick J. Donnelly
from ..pieces import Piece

class MoveLogic:
    """Represents the move-level logic of the program"""
    def __init__(self, board_logic):
        self.board_logic = board_logic

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
                self.board_logic.abort_move()
            else:
                # If the pieces are on opposite teams, attempt capture; else, abort
                if square.piece.team != square.container.move:
                    self.attempt_capture(square)
                else:
                    self.board_logic.abort_move()
        elif square.piece.team == square.container.move:
            square.container.selected_square = square
            if self.board_logic.has_legal_moves():
                self.board_logic.highlight_legal_moves()
            else:
                self.board_logic.abort_move()

    def attempt_capture(self, square):
        """
        Attempts to capture the current square from the board's selected square
        :param square: sic.
        """
        # If the attempted ove is legal, execute; else, abort
        if self.board_logic.legality_logic.is_legal(square):
            self.move(square)
            square.container.move = not square.container.move
            self.board_logic.remove_highlights()
            self.update(square)
            self.board_logic.gui.update_menu()
        else:
            self.board_logic.abort_move()

    def move(self, square):
        """
        Moves one piece from the given space to the selected space
        :param square: sic.
        """
        self.board_logic.board.selected_square.piece.has_moved = True
        square.piece = square.container.selected_square.piece
        square.container.selected_square.piece = Piece(None)

    def update(self, square):
        """
        Updates the two squares involved in a move as opposed to the whole board
        :param square: sic.
        """
        self.board_logic.board.selected_square.update()
        square.update()
        square.container.selected_square = None
