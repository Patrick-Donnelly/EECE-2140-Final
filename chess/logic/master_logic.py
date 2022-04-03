# master_logic.py by Patrick J. Donnelly
# The main logic module for the chess game
from .general_movement import *
from .piece_movement import *
from ..square import Square

def master_button_action(square: Square):
    """
    Sice Tkinter buttons can only have one command, this function serves as that command
    :param square: The square attached to the button
    """
    # If there is a highlighted square, either attempt or abort capture
    # If you attempt to highlight an enemy or null piece, nothing happens
    if square.container.selected_square:
        # If the selected square is the given square, abort capture
        if square.container.selected_square is square:
            abort_move(square.container)
        else:
            # If the pieces are on opposite teams, attempt capture; else, abort
            if square.piece.team != square.container.move:
                attempt_capture(square)
            else:
                abort_move(square.container)
    elif square.piece.team == square.container.move:
        square.container.selected_square = square
        if has_legal_moves(square.container):
            highlight_legal_moves(square.container)
        else:
            abort_move(square.container)

def attempt_capture(square: Square):
    """
    Attempts to capture the current square from the board's selected square
    :param square: sic.
    """
    # If the attempted ove is legal, execute; else, abort
    if is_legal(square.container, square):
        move(square)
        square.container.move = not square.container.move
        remove_highlights(square.container)
        update(square)
    else:
        abort_move(square.container)

def update(square: Square):
    """
    Updates the two squares involved in a move as opposed to the whole board
    :param square: sic.
    """
    square.container.selected_square.update()
    square.update()
    square.container.selected_square = None
