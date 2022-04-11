# legality_logic.py by Patrick J. Donnelly
from ..pieces import *

# NOTE: The coordinate system for this is unusual. All coordinates are relative to the forward direction of the piece.

class LegalityLogic:
    def __init__(self, move_logic):
        self.move_logic = move_logic

    def is_legal(self, square) -> bool:
        """
        A bloated switch to direct move to proper logic
        :param square: ditto
        """
        attacker = self.move_logic.board_logic.board.selected_square.piece

        if square.piece.team == attacker.team:
            return False

        if isinstance(attacker, Pawn):
            return self.is_legal_pawn(square)
        elif isinstance(attacker, Knight):
            return self.is_legal_knight(square)
        elif isinstance(attacker, Bishop):
            return self.is_legal_bishop(square)
        elif isinstance(attacker, Rook):
            return self.is_legal_rook(square)
        elif isinstance(attacker, Queen):
            return self.is_legal_queen(square)
        elif isinstance(attacker, King):
            return self.is_legal_king(square)
        else:
            raise RuntimeError("UNKNOWN ERROR")

    def is_legal_pawn(self, defender) -> bool:
        """
        Determines the legality of a given pawn move
        :param defender: The defending square
        :return: A Boolean corresponding to the legality of the move
        """
        attacker = self.move_logic.board_logic.board.selected_square
        dx, dy = self.get_dp(attacker, defender)

        # The most basic chess piece, can only move forward, and may only capture diagonally
        if dy == 0:  # Must either be a first-move move of two, or a simple move of one; must be unobstructed
            if dx == 2 and not attacker.piece.has_moved:
                return not (bool(self.get_relative(1, 0).piece) and bool(attacker.piece))
            elif dx == 1:
                return not bool(defender.piece)
            else:
                return False
        elif dy in [-1, 1]:  # By definition, must either be attempting to capture or is an illegal move
            if dx == 1:
                return bool(defender.piece) or self.check_en_passant(defender)
            else:
                return False
        else:
            return False

    def is_legal_knight(self, defender) -> bool:
        """
        Determines the legality of a given knight move
        :param defender: The defending square
        :return: A Boolean corresponding to the legality of the move
        """
        attacker = self.move_logic.board_logic.board.selected_square
        dx, dy = self.get_dp(attacker, defender)
        dx, dy = abs(dx), abs(dy)

        # The knight can only move in L shapes
        if dx in [1, 2] and dy in [1, 2]:
            return dx != dy
        else:
            return False

    def is_legal_bishop(self, defender) -> bool:
        """
        Determines the legality of a given bishop move
        :param defender: The defending square
        :return: A Boolean corresponding to the legality of the move
        """
        attacker = self.move_logic.board_logic.board.selected_square
        dx, dy = self.get_dp(attacker, defender)

        # Bishop can only move along diagonals, i.e. |dx| = |dy| with no other pieces in the way
        if abs(dx) == abs(dy):
            x_negative = dx < 0
            y_negative = dy < 0
            # For each square along the diagonal, if it is populated by a non-null piece, it fails
            for i in range(1, abs(dx)):
                if bool(self.get_relative(i*((-1)**x_negative), i*((-1)**y_negative)).piece):
                    return False
            return True
        else:
            return False

    def is_legal_rook(self, defender) -> bool:
        """
        Determines the legality of a given rook move
        :param defender: The defending square
        :return: A Boolean corresponding to the legality of the move
        """
        attacker = self.move_logic.board_logic.board.selected_square
        dx, dy = self.get_dp(attacker, defender)

        # Rooks may only move in straight lines
        if (dx == 0) != (dy == 0):  # Logical XOR; one must be zero, but not both
            # For each square along the rank or file, if it is populated by a non-null piece, it fails
            if dx:
                x_negative = dx < 0
                for i in range(1, abs(dx)):
                    if bool(self.get_relative(i*((-1)**x_negative), 0).piece):
                        return False
            else:
                y_negative = dy < 0
                for i in range(1, abs(dy)):
                    if bool(self.get_relative(0, i*((-1)**y_negative)).piece):
                        return False
            return True
        else:
            return False

    def is_legal_queen(self, defender) -> bool:
        """
        Determines the legality of a given rook move
        :param defender: The defending square
        :return: A Boolean corresponding to the legality of the move
        """
        # A queen is a combination a bishop and a rook
        return self.is_legal_bishop(defender) or self.is_legal_rook(defender)

    def is_legal_king(self, defender) -> bool:
        """
        Determines the legality of a given rook move
        :param defender: The defending square
        :return: A Boolean corresponding to the legality of the move
        """
        attacker = self.move_logic.board_logic.board.selected_square
        dx, dy = self.get_dp(attacker, defender)

        # A king can only move one space in any direction, including diagonals
        if dx in [-1, 0, 1] and dy in [-1, 0, 1]:
            return True
        else:
            return self.check_castle(defender)

    def check_en_passant(self, defender) -> bool:
        attacker = self.move_logic.board_logic.board.selected_square
        dx, dy = self.get_dp(attacker, defender)

        if dy == -1:
            piece = self.get_relative(0, -1).piece
        else:
            piece = self.get_relative(0, 1).piece

        return piece is self.move_logic.en_passant

    def check_castle(self, defender) -> bool:
        squares = self.move_logic.board_logic.board.squares
        attacker = self.move_logic.board_logic.board.selected_square

        if defender.rank in [0, 7] and defender.file in [2, 6] and not attacker.piece.has_moved:
            rook = squares[7*attacker.piece.team][7*(defender.file == 6)]
            return isinstance(rook.piece, Rook) and not rook.piece.has_moved and self.is_legal_rook(defender)
        else:
            return False

    @staticmethod
    def get_dp(attacker, defender) -> (int, int):
        """
        Returns the difference in position of the defending square relative to the attacking piece
        :param attacker: ditto
        :param defender: ditto
        :return: A tuple in the form of dx, dy
        """
        if attacker.piece.team:
            return attacker.rank - defender.rank, defender.file - attacker.file
        else:
            return defender.rank - attacker.rank, attacker.file - defender.file

    # NOTE: COORDINATES ARE BACKWARD FROM MATHEMATICAL CONVENTION
    def get_relative(self, dx: int, dy: int):
        """
        Returns the square relative to a given square via standardized units
        :param dx: VERTICAL DISPLACEMENT
        :param dy: HORIZONTAL DISPLACEMENT
        """
        square = self.move_logic.board_logic.board.selected_square
        x = square.rank
        y = square.file
        if square.piece.team:
            return self.move_logic.board_logic.board.squares[x-dx][y+dy]
        else:
            return self.move_logic.board_logic.board.squares[x+dx][y-dy]
