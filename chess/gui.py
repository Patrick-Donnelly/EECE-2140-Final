# gui.py by Patrick J. Donnelly
from tkinter import Tk, Button, ACTIVE, DISABLED

class GUI:
    """The beating heart of the chess program; handles TkInterface objects"""
    def __init__(self):
        from .board import Board

        self.root = Tk()

        # Creates a non-resizable 640x720 window named 'Chess' situated on top of all windows
        self.root.title("Chess")
        self.root.geometry('640x720')
        self.root.resizable(False, False)
        self.root.wm_attributes('-topmost', True)

        # Call and place the chessboard, which will initialize itself upon instantiation
        self.board = Board(self.root)

        self.generate_menu()

    def generate_menu(self):
        """
        Creates the menu of buttons placed below the chessboard
        """
        from .logic.menuing import reset_game, flip_board

        H, W, P = 4, 16, 2  # Height, Width, Pad
        reset = Button(self.root, height=H, width=W, text="RESTART", command=lambda: reset_game(self.board))
        flip = Button(self.root, height=H, width=W, text="FLIP BOARD", command=lambda: flip_board(self.board))
        undo = Button(self.root, height=H, width=W, text="UNDO MOVE")
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
