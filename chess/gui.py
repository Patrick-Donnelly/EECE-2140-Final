# gui.py by Patrick J. Donnelly
from tkinter import Tk, Button
from .board import Board

from .logic.initialization import BLACK, WHITE, H, W, P

class GUI:
    """The beating heart of the chess program; handles TkInterface objects"""
    def __init__(self):
        self.root = Tk()

        self.reset = None
        self.flip = None
        self.indicator = None
        self.end = None

        # Creates a non-resizable 640x720 window named 'Chess' situated on top of all windows
        self.root.title("Chess")
        self.root.geometry('640x720')
        self.root.resizable(False, False)
        self.root.wm_attributes('-topmost', True)

        # Call and place the chessboard, which will initialize itself upon instantiation
        self.board = Board(self.root)

        self.update_menu()

    def update_menu(self):
        """
        Creates the menu of buttons placed below the chessboard
        """
        self.delete_menu()

        bg = self.get_bg()
        fg = self.get_fg()

        self.reset = Button(self.root, height=H, width=W, bg=bg, fg=fg, text="RESTART",
                            command=lambda: self.board.reset_game())
        self.flip = Button(self.root, height=H, width=W, bg=bg, fg=fg, text="FLIP BOARD",
                           command=lambda: self.board.flip_board())
        self.indicator = Button(self.root, height=H, width=W, bg=bg, fg=fg, text=self.get_text(),
                                command=lambda: self.board.set_view())
        self.end = Button(self.root, height=H, width=W, bg=bg, fg=fg, text="EXIT",
                          command=lambda: self.root.destroy())

        self.reset.grid(row=9, rowspan=1, column=0, columnspan=2, padx=P)
        self.flip.grid(row=9, rowspan=1, column=2, columnspan=2, padx=P)
        self.indicator.grid(row=9, rowspan=1, column=4, columnspan=2, padx=P)
        self.end.grid(row=9, rowspan=1, column=6, columnspan=2, padx=P)

    def delete_menu(self):
        """
        Deletes the contents of the current menu
        """
        if self.reset:
            self.reset.destroy()
        if self.flip:
            self.flip.destroy()
        if self.indicator:
            self.indicator.destroy()
        if self.end:
            self.end.destroy()

    def get_bg(self) -> str:
        if self.board.move:
            return WHITE
        else:
            return BLACK

    def get_fg(self) -> str:
        if self.board.move:
            return BLACK
        else:
            return WHITE

    def get_text(self) -> str:
        if self.board.move:
            return "WHITE TO MOVE"
        else:
            return "BLACK TO MOVE"

    def begin_game(self):
        """
        Begins the game by initiating main loop
        """
        self.root.mainloop()
