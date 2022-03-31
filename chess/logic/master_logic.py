# master_logic.py by Patrick J. Donnelly
# The main logic module for the chess game
from .movement import *

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
    update()

def attempt_capture(board: Board, square: Square):
    if is_legal(board, square):
        pass

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


def update():
    pass
