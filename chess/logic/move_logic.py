# move_logic.py by Patrick J. Donnelly
from ..pieces import Piece, King, Queen, Pawn

class MoveLogic:
    """Represents the move-level logic of the program"""
    def __init__(self, board_logic):
        self.board_logic = board_logic
        self.en_passant = None

    def attempt_capture(self, defender):
        """
        Attempts to capture the current square from the board's selected square
        :param defender: ditto
        """
        # If the attempted move is legal, execute; else, abort
        if self.board_logic.legality_logic.is_legal(defender):
            if self.board_logic.check:
                self.board_logic.end_check()
            self.en_passant = None
            self.move(defender)

            # Pawn automatically promotes to queen
            if isinstance(defender.piece, Pawn):
                if defender.piece.team and defender.rank == 0:
                    defender.piece = Queen(True)
                elif not defender.piece.team and defender.rank == 7:
                    defender.piece = Queen(False)
                defender.update()

            defender.container.move = not defender.container.move
            self.board_logic.remove_highlights()
            self.board_logic.gui.update_menu()
        else:
            self.board_logic.abort_move()

    def move(self, defender):
        """
        Moves one piece from the given space to the selected space
        :param defender: ditto
        """
        attacker = self.board_logic.board.selected_square
        self.check_castle(defender)
        self.check_en_passant(defender)

        if isinstance(defender.piece, King):
            self.board_logic.board.kings[not self.board_logic.board.move] = None

        if isinstance(attacker.piece, King):
            self.board_logic.board.kings[self.board_logic.board.move] = defender

        self._move(attacker, defender)
        self.board_logic.board.selected_square = None

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

    def check_en_passant(self, defender):
        """
        Handles movement logic for en passant
        :param defender: ditto
        """
        attacker = self.board_logic.board.selected_square

        if not isinstance(attacker.piece, Pawn):
            return

        dp = self.board_logic.legality_logic.get_dp(self.board_logic.board.selected_square, defender)

        # En passant may only be executed immediately following the opponent's two-space pawn move
        if dp == (2, 0):
            self.en_passant = attacker.piece

        if dp in [(1, -1), (1, 1)] and not defender.piece:
            logic = self.board_logic.legality_logic
            pawn_square = logic.get_relative(attacker, 0, dp[1])
            pawn_square.piece = Piece(None)
            pawn_square.update()

    def check_castle(self, defender):
        """
        Handles the movement logic in the event of a castle
        :param defender: ditto
        """
        attacker = self.board_logic.board.selected_square

        if not isinstance(attacker.piece, King) or attacker.piece.has_moved:
            return

        dp = self.board_logic.legality_logic.get_dp(self.board_logic.board.selected_square, defender)

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
            self._move(logic.get_relative(attacker, 0, rook), logic.get_relative(attacker, 0, target))
