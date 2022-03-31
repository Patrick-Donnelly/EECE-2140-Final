# movement.py by Patrick J. Donnelly
from ..board import Board
from ..square import Square
from ..pieces import *

def is_legal_pawn(board: Board, square: Square) -> bool:
    pass

def is_legal_knight(board: Board, square: Square) -> bool:
    pass

def is_legal_bishop(board: Board, square: Square) -> bool:
    pass

def is_legal_rook(board: Board, square: Square) -> bool:
    pass

def is_legal_queen(board: Board, square: Square) -> bool:
    pass

def is_legal_king(board: Board, square: Square) -> bool:
    pass

def get_dp(piece: Piece, square: Square):
    """
    Returns the orthogonal difference in position between a piece and a square
    :param piece: sic.
    :param square: sic.
    :return: A tuple in the form dx, dy
    """
    if not square.container.is_flipped:
        return piece.rank - square.rank, piece.file - square.file
    else:
        return square.rank - piece.rank, square.file - piece.file
