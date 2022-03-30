# gui.py by Patrick J. Donnelly
from tkinter import Tk, Button
from .board import Board
from .logic.master_logic import reset_game, flip_board, undo_last_move

class GUI:
    """The beating heart of the chess program; handles TkInterface objects"""
    def __init__(self):
        self.root = Tk()

        # Creates a non-resizable 640x720 window named 'Chess'
        self.root.title("Chess")
        self.root.geometry('640x720')
        self.root.resizable(False, False)

        # Call and place the chessboard
        self.board = Board(self.root)

        self.generate_menu()

    def generate_menu(self):
        """
        Creates the menu of buttons placed below the chessboard
        """
        H, W, P = 4, 16, 2  # Height, Width, Pad
        reset = Button(self.root, height=H, width=W, text="RESTART", command=reset_game)
        flip = Button(self.root, height=H, width=W, text="FLIP BOARD", command=flip_board)
        undo = Button(self.root, height=H, width=W, text="UNDO MOVE", command=undo_last_move)
        end = Button(self.root, height=H, width=W, text="EXIT", command=lambda: self.root.destroy())

        reset.grid(row=9, rowspan=1, column=0, columnspan=2, padx=P)
        flip.grid(row=9, rowspan=1, column=2, columnspan=2, padx=P)
        undo.grid(row=9, rowspan=1, column=4, columnspan=2, padx=P)
        end.grid(row=9, rowspan=1, column=6, columnspan=2, padx=P)

    def begin_game(self):
        """
        Begins the game by initiating main loop
        """
        self.root.mainloop()
