# gui.py by Patrick J. Donnelly
from tkinter import Tk, Button, RAISED
from .board import Board
from .logic.initialization import BG, BLACK, WHITE, H, W, PX, PY, BW

class GUI:
    """The beating heart of the chess program; handles TkInterface objects and contains lesser containers"""
    def __init__(self):
        """Creates and initializes the game GUI"""
        # Creates the root window for the game
        self.root = Tk()

        # Menu button placeholders
        self.reset = None
        self.flip = None
        self.indicator = None
        self.end = None

        # Creates a non-resizable 640x720 window named 'Chess' situated on top of all windows
        self.root.title("Chess")
        self.root.geometry('640x720')
        self.root.resizable(False, False)
        self.root.wm_attributes('-topmost', True)
        self.root.config(bg=BG)

        # Call and place the chessboard, which will initialize itself upon instantiation
        self.board = Board(self.root, self)

        # Initializes the menu
        self.update_menu()

    def update_menu(self):
        """
        Creates the menu of buttons placed below the chessboard
        """
        # Deletes the current menu, if present
        self.delete_menu()

        # Get background and foreground colors for menu; changes depending on next move
        bg = WHITE if self.board.move else BLACK
        fg = BLACK if self.board.move else WHITE
        text = "WHITE TO MOVE" if self.board.move else "BLACK TO MOVE"

        self.reset = Button(self.root, height=H, width=W, bg=bg, fg=fg, text="RESTART", relief=RAISED, borderwidth=BW,
                            command=lambda: self.board.reset_game())
        self.flip = Button(self.root, height=H, width=W, bg=bg, fg=fg, text="FLIP BOARD", relief=RAISED, borderwidth=BW,
                           command=lambda: self.board.flip_board())
        self.indicator = Button(self.root, height=H, width=W, bg=bg, fg=fg, text=text, relief=RAISED, borderwidth=BW,
                                command=lambda: self.board.set_view())
        self.end = Button(self.root, height=H, width=W, bg=bg, fg=fg, text="EXIT", relief=RAISED, borderwidth=BW,
                          command=lambda: self.root.destroy())

        self.reset.grid(row=9, rowspan=1, column=0, columnspan=2, padx=PX, pady=PY)
        self.flip.grid(row=9, rowspan=1, column=2, columnspan=2, padx=PX, pady=PY)
        self.indicator.grid(row=9, rowspan=1, column=4, columnspan=2, padx=PX, pady=PY)
        self.end.grid(row=9, rowspan=1, column=6, columnspan=2, padx=PX, pady=PY)

    def delete_menu(self):
        """
        Deletes the contents of the current menu, if it exists
        """
        # For each button, if it exists, delete it via tkinter.Button.destroy()
        if self.reset:
            self.reset.destroy()
        if self.flip:
            self.flip.destroy()
        if self.indicator:
            self.indicator.destroy()
        if self.end:
            self.end.destroy()

    def begin_game(self):
        """
        Begins the game by initiating main loop
        """
        self.root.mainloop()
