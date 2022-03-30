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
    pass
