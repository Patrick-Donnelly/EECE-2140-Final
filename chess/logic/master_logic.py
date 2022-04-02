# master_logic.py by Patrick J. Donnelly
# The main logic module for the chess game
from .movement import *
from ..square import Square

def master_button_action(board: Board, square: Square):
    """
    Sice Tkinter buttons can only have one command, this function serves as that command
    :param board: The board attached to the button
    :param square: The square attached to the button
    """
    # If there is a highlighted square, either attempt or abort capture
    # If you attempt to highlight an enemy or null piece, nothing happens
    if board.selected_square:
        # If the selected square is the given square, abort capture
        if board.selected_square is square:
            board.selected_square = None
        else:
            # If the pieces are on opposite teams, attempt capture; else, abort
            if square.piece.team != board.move:
                attempt_capture(board, square)
            else:
                board.selected_square = None
    elif square.piece.team == board.move:
        board.selected_square = square

def attempt_capture(board: Board, square: Square):
    """
    Attempts to capture the current square from the board's selected square
    :param board: sic.
    :param square: sic.
    """
    # If the attempted ove is legal, execute; else, abort
    if is_legal(board, square):
        move(board, square)
        board.move = not board.move
        update(board, square)
    else:
        board.selected_square = None

def is_legal(board: Board, square: Square) -> bool:
    """
    A bloated switch to direct move to proper logic
    :param board: sic.
    :param square: sic.
    """
    attacker = board.selected_square.piece

    if isinstance(attacker, Pawn):
        return is_legal_pawn(board, square)
    elif isinstance(attacker, Knight):
        return is_legal_pawn(board, square)
    elif isinstance(attacker, Bishop):
        return is_legal_pawn(board, square)
    elif isinstance(attacker, Rook):
        return is_legal_pawn(board, square)
    elif isinstance(attacker, Queen):
        return is_legal_pawn(board, square)
    elif isinstance(attacker, King):
        return is_legal_pawn(board, square)
    else:
        raise RuntimeError("UNKNOWN ERROR")

def move(board: Board, square: Square):
    """
    Moves one piece from the given space to the selected space
    :param board: sic.
    :param square: sic.
    """
    board.selected_square.piece.has_moved = True
    square.piece = board.selected_square.piece
    board.selected_square.piece = Piece(None)

def update(board: Board, square: Square):
    """
    Updates the two squares involved in a move as opposed to the whole board
    :param board: sic.
    :param square: sic.
    """
    board.selected_square.update_square()
    square.update_square()
    board.selected_square = None
