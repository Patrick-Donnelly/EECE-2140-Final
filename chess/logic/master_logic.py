# master_logic.py by Patrick J. Donnelly
# The main logic module for the chess game
from ..board import Board
from ..square import Square
from ..pieces import *

def master_button_action(board: Board, square: Square):
    # If there is a highlighted square, either attempt or abort capture
    if board.selected_square:
        # If the selected square is the given square, abort capture
        if board.selected_square is square:
            board.selected_square = None
            increment_move(board, -1)
        else:
            # If the pieces are on opposite teams, attempt capture; else, abort
            if square.piece.team != get_team(board):
                attempt_capture(board, square)
            else:
                board.selected_square = None
                increment_move(board, -1)
    elif square.piece.team == get_team(board):
        board.selected_square = square
        increment_move(board, 1)
    update()

def get_team(board: Board):
    return board.move in [0, 1]

def increment_move(board: Board, val: int):
    board.move = (board.move + val) % 4

def attempt_capture(board: Board, square: Square):
    pass

def update():
    pass
