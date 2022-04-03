# general_movement.py by Patrick J. Donnelly
from .piece_movement import *

def abort_move(board: Board):
    """
    Resets the board to a selection state
    :param board: sic.
    """
    board.selected_square = None
    remove_highlights(board)

def has_legal_moves(board: Board) -> bool:
    """
    Determines whether a given piece has legal moves
    :param board: sic.
    :return: A Boolean representing whether a given piece has legal moves
    """
    for rank in board.squares:
        for square in rank:
            if is_legal(board, square):
                return True
    return False

def highlight_legal_moves(board: Board):
    """
    Highlights all the legal spaces available to the selected piece
    :param board: sic.
    """
    board.selected_square.is_inverted = True
    board.selected_square.update()

    for rank in board.squares:
        for square in rank:
            if is_legal(board, square):
                square.is_inverted = True
                square.update()

def remove_highlights(board: Board):
    """
    Removes any highlighting from all squares on the board
    :param board: sic.
    """
    for rank in board.squares:
        for square in rank:
            if square.is_inverted:
                square.is_inverted = False
                square.update()

def move(square: Square):
    """
    Moves one piece from the given space to the selected space
    :param square: sic.
    """
    square.container.selected_square.piece.has_moved = True
    square.piece = square.container.selected_square.piece
    square.container.selected_square.piece = Piece(None)
