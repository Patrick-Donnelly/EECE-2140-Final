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
        remove_highlights(board)
        update(board, square)
    else:
        abort_move(board)

def is_legal(board: Board, square: Square) -> bool:
    """
    A bloated switch to direct move to proper logic
    :param board: sic.
    :param square: sic.
    """
    attacker = board.selected_square.piece

    if square.piece.team == attacker.team:
        return False

    if isinstance(attacker, Pawn):
        return is_legal_pawn(board, square)
    elif isinstance(attacker, Knight):
        return is_legal_knight(board, square)
    elif isinstance(attacker, Bishop):
        return is_legal_bishop(board, square)
    elif isinstance(attacker, Rook):
        return is_legal_rook(board, square)
    elif isinstance(attacker, Queen):
        return is_legal_queen(board, square)
    elif isinstance(attacker, King):
        return is_legal_king(board, square)
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
    board.selected_square.update()
    square.update()
    board.selected_square = None
