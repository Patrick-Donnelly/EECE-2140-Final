# movement.py by Patrick J. Donnelly
from ..board import Board
from ..square import Square
from ..pieces import *

# NOTE: The coordinate system for this will get very messy, so I am going to explain my system here. Due to my wanting
# to keep the logic to a minimum and maintain the ability to flip the board, all comparisons will be piece neutral and
# relative to the attacking piece. That is, if a white piece is at rank = x = 3, the piece immediately in front of it
# will be rank = x = 4, with the exact same coordinates working for a black piece.

def is_legal_pawn(board: Board, defender: Square) -> bool:
    """
    Determines the legality of a given pawn move
    :param board: sic.
    :param defender: The defending square
    :return: A Boolean corresponding to the legality of the move
    """
    attacker = board.selected_square
    dx, dy = get_dp(attacker, defender)
    print(dx, dy)
    print(attacker.piece.has_moved)

    # The most basic chess piece, can only move forward, and may only capture sideways
    if dy == 0:
        if dx == 2 and not attacker.piece.has_moved:
            return not (bool(get_relative(board, 1, 0).piece) and bool(attacker.piece))
        elif dx == 1:
            return not bool(defender.piece)
        else:
            return False
    elif dy in [-1, 1]:
        if dx == 1:
            return bool(defender.piece)
        else:
            return False
    else:
        return False

def is_legal_knight(attacker: Square, defender: Square) -> bool:
    pass

def is_legal_bishop(attacker: Square, defender: Square) -> bool:
    pass

def is_legal_rook(attacker: Square, defender: Square) -> bool:
    pass

def is_legal_queen(attacker: Square, defender: Square) -> bool:
    pass

def is_legal_king(attacker: Square, defender: Square) -> bool:
    pass

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
