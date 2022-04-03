# menuing.py by Patrick J. Donnelly
from ..board import Board

def flip_board(board: Board):
    board.is_flipped = not board.is_flipped
    board.update_squares()

def reset_game(board: Board):
    board.make_squares()
    board.move = True
    board.is_flipped = False
    # Doesn't require an update command because squares are destroyed and re-instantiated

def undo_last_move():
    pass
