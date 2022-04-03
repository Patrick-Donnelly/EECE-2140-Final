# menuing.py by Patrick J. Donnelly
from ..board import Board
H, W, P = 4, 16, 2  # Height, Width, Pad
BLACK = '#000000'
WHITE = '#ffffff'

def flip_board(board: Board):
    board.is_flipped = not board.is_flipped
    board.update_squares()

def reset_game(board: Board):
    board.move = True
    board.is_flipped = False
    board.make_squares()
    # Doesn't require an update command because squares are destroyed and re-instantiated

def set_view(board: Board):
    if board.move == board.is_flipped:
        flip_board(board)

def get_bg(move: bool) -> str:
    if move:
        return WHITE
    else:
        return BLACK

def get_fg(move: bool) -> str:
    if move:
        return BLACK
    else:
        return WHITE

def get_text(move: bool) -> str:
    if move:
        return "WHITE TO MOVE"
    else:
        return "BLACK TO MOVE"
