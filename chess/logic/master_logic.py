# master_logic.py by Patrick J. Donnelly
# The main logic module for the chess game
from .general_movement import *
from .piece_movement import *
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
            abort_move(board)
        else:
            # If the pieces are on opposite teams, attempt capture; else, abort
            if square.piece.team != board.move:
                attempt_capture(board, square)
            else:
                abort_move(board)
    elif square.piece.team == board.move:
        board.selected_square = square
        if has_legal_moves(board):
            highlight_legal_moves(board)
        else:
            abort_move(board)

def attempt_capture(board: Board, square: Square):
    """
    Attempts to capture the current square from the board's selected square
    :param board: sic.
    :param square: sic.
    """
    # If the attempted ove is legal, execute; else, abort
    if is_legal(board, square):
        board.container.history.append(board)
        move(board, square)
        board.move = not board.move
        remove_highlights(board)
        update(board, square)
    else:
        abort_move(board)

def update(board: Board, square: Square):
    """
    Updates the two squares involved in a move as opposed to the whole board
    :param board: sic.
    :param square: sic.
    """
    board.selected_square.update()
    square.update()
    board.selected_square = None
