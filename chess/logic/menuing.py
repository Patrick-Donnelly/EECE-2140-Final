# menuing.py by Patrick J. Donnelly
from ..board import Board

def flip_board(board: Board):
    board.is_flipped = not board.is_flipped
    update_all()

def reset_game(board: Board):
    board.make_squares()
    update_all()

def undo_last_move():
    pass

def update_all():
    pass
