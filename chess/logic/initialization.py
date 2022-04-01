# initialization.py by Patrick J. Donnelly
from ..pieces import *

# Hex colors for black and white squares
WHITE_SQUARE = '#bfbfbf'
BLACK_SQUARE = '#994d00'

def get_color(rank: int, file: int) -> str:
    """
    A simple formula for determining the appropriate color for the square
    :param rank: The rank (row) of the square
    :param file: The file (column) of the square
    :return: A string corresponding to the appropriate background color of the square
    """
    # Using taxicab distance, determine proper color
    if (rank + file) % 2 == 0:
        return WHITE_SQUARE
    else:
        return BLACK_SQUARE

def get_piece(rank: int, file: int) -> Piece:
    """
    Returns the appropriate starting piece for a given space
    :param rank: The rank of the Square
    :param file: The file of the Square
    :return: The said appropriate piece
    """
    if rank == 1:  # Black pawns
        return Pawn(False)
    elif rank == 6:  # White pawns
        return Pawn(True)
    elif rank in [0, 7]:  # It's chess
        if file in [0, 7]:
            return Rook(rank == 7)
        elif file in [1, 6]:
            return Knight(rank == 7)
        elif file in [2, 5]:
            return Bishop(rank == 7)
        elif file == 3:
            return Queen(rank == 7)
        elif file == 4:
            return King(rank == 7)
        else:
            raise ValueError("RANK AND FILE OUTSIDE BOARD DIMENSIONS")
    else:
        return Piece(None)  # For the sake of generality, spaces without pieces get null pieces
