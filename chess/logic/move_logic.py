# move_logic.py by Patrick J. Donnelly
from ..pieces import Piece, King

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
        :param square: ditto
        """
        # If the attempted ove is legal, execute; else, abort
        if self.board_logic.legality_logic.is_legal(square):
            self.move(square)
            square.container.move = not square.container.move
            self.board_logic.remove_highlights()
            self.board_logic.gui.update_menu()
        else:
            self.board_logic.abort_move()

    def move(self, defender):
        """
        Moves one piece from the given space to the selected space
        :param defender: ditto
        """
        self.check_castle(defender)
        self._move(self.board_logic.board.selected_square, defender)
        defender.container.selected_square = None

    @staticmethod
    def _move(attacker, defender):
        """
        Moves one piece unto a given square
        :param attacker: ditto
        :param defender: ditto
        """
        attacker.piece.has_moved = True
        defender.piece = attacker.piece
        attacker.piece = Piece(None)
        attacker.update()
        defender.update()

    def check_castle(self, square):
        """
        Handles the movement logic in the event of a castle
        :param square: ditto
        """
        attacker = self.board_logic.board.selected_square

        if not isinstance(attacker.piece, King) or attacker.piece.has_moved:
            return

        dp = self.board_logic.legality_logic.get_dp(self.board_logic.board.selected_square, square)

        # Since the rook and target are asymmetric across teams, but stay on the same rank, we can calculate dy and
        # extrapolate using the above generalized move function
        if dp in [(0, -2), (0, 2)]:
            if dp == (0, -2):
                rook = -4 if attacker.piece.team else -3
                target = -1
            else:
                rook = 3 if attacker.piece.team else 4
                target = 1

            logic = self.board_logic.legality_logic
            self._move(logic.get_relative(0, rook), logic.get_relative(0, target))
