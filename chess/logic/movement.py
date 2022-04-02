# movement.py by Patrick J. Donnelly
from ..board import Board
from ..square import Square
from ..pieces import *

# NOTE: The coordinate system for this is unusual. All coordinates are relative to the forward direction of the piece.

def is_legal_pawn(board: Board, defender: Square) -> bool:
    """
    Determines the legality of a given pawn move
    :param board: sic.
    :param defender: The defending square
    :return: A Boolean corresponding to the legality of the move
    """
    attacker = board.selected_square
    dx, dy = get_dp(attacker, defender)

    # The most basic chess piece, can only move forward, and may only capture diagonally
    if dy == 0:  # Must either be a first-move move of two, or a simple move of one; must be unobstructed
        if dx == 2 and not attacker.piece.has_moved:
            return not (bool(get_relative(board, 1, 0).piece) and bool(attacker.piece))
        elif dx == 1:
            return not bool(defender.piece)
        else:
            return False
    elif dy in [-1, 1]:  # By definition, must either be attempting to capture or is an illegal move
        if dx == 1:
            return bool(defender.piece)
        else:
            return False
    else:
        return False

def is_legal_knight(board: Board, defender: Square) -> bool:
    """
    Determines the legality of a given knight move
    :param board: sic.
    :param defender: The defending square
    :return: A Boolean corresponding to the legality of the move
    """
    attacker = board.selected_square
    dx, dy = get_dp(attacker, defender)
    dx, dy = abs(dx), abs(dy)

    # The knight can only move in L shapes
    if dx in [1, 2] and dy in [1, 2]:
        return dx != dy
    else:
        return False

def is_legal_bishop(board: Board, defender: Square) -> bool:
    """
    Determines the legality of a given bishop move
    :param board: sic.
    :param defender: The defending square
    :return: A Boolean corresponding to the legality of the move
    """
    attacker = board.selected_square
    dx, dy = get_dp(attacker, defender)

    # Bishop can only move along diagonals, i.e. |dx| = |dy| with no other pieces in the way
    if abs(dx) == abs(dy):
        x_negative = dx < 0
        y_negative = dy < 0
        # For each square along the diagonal, if it is populated by a non-null piece, it fails
        for i in range(1, abs(dx)):
            if bool(get_relative(board, i*((-1)**x_negative), i*((-1)**y_negative)).piece):
                return False
        return True
    else:
        return False

def is_legal_rook(board: Board, defender: Square) -> bool:
    """
    Determines the legality of a given rook move
    :param board: sic.
    :param defender: The defending square
    :return: A Boolean corresponding to the legality of the move
    """
    attacker = board.selected_square
    dx, dy = get_dp(attacker, defender)

    # Rooks may only move in straight lines
    if (dx == 0) != (dy == 0):  # Logical XOR; one must be zero, but not both
        # For each square along the rank or file, if it is populated by a non-null piece, it fails
        if dx:
            x_negative = dx < 0
            for i in range(1, abs(dx)):
                if bool(get_relative(board, i*((-1)**x_negative), 0).piece):
                    return False
        else:
            y_negative = dy < 0
            for i in range(1, abs(dy)):
                if bool(get_relative(board, 0, i*((-1)**y_negative)).piece):
                    return False
        return True
    else:
        return False

def is_legal_queen(board: Board, defender: Square) -> bool:
    """
    Determines the legality of a given rook move
    :param board: sic.
    :param defender: The defending square
    :return: A Boolean corresponding to the legality of the move
    """
    # A queen is a combination bishop and rook
    return is_legal_bishop(board, defender) or is_legal_rook(board, defender)

def is_legal_king(board: Board, defender: Square) -> bool:
    """
    Determines the legality of a given rook move
    :param board: sic.
    :param defender: The defending square
    :return: A Boolean corresponding to the legality of the move
    """
    attacker = board.selected_square
    dx, dy = get_dp(attacker, defender)

    # A king can only move one space in any direction, including diagonals
    if dx in [-1, 0, 1] and dy in [-1, 0, 1]:
        return True
    else:
        return False

def get_dp(attacker: Square, defender: Square) -> (int, int):
    """
    Returns the difference in position of the defending square relative to the attacking piece
    :param attacker: sic.
    :param defender: sic.
    :return: A tuple in the form of dx, dy
    """
    if attacker.piece.team:
        return attacker.rank - defender.rank, defender.file - attacker.file
    else:
        return defender.rank - attacker.rank, attacker.file - defender.file

def get_relative(board: Board, dx: int, dy: int) -> Square:
    """
    Returns the square relative to a given square via standardized units
    :param board: sic.
    :param dx: sic.
    :param dy: sic.
    """
    x, y = board.selected_square.rank, board.selected_square.file
    if board.selected_square.piece.team:
        return board.squares[x - dx][y + dy]
    else:
        return board.squares[x + dx][y - dy]
