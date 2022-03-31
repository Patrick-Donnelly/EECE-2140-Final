# square.py by Patrick J. Donnelly
from tkinter import Frame, Button
from tkinter.font import Font

class Square:
    """An abstraction of a chessboard square to hold Piece() objects with TkInterface properties"""
    def __init__(self, master: Frame, container, rank: int, file: int,
                 color: str, rank_label=None, file_label=None):
        from .logic.initialization import get_piece

        self.master = master
        self.container = container

        self.rank = rank
        self.file = file
        self.rank_label = rank_label
        self.file_label = file_label

        self.color = color
        self.piece = get_piece(self, rank, file)
        self.font = None

        self.square = None

        self.set_square()

    def set_square(self):
        """
        Set the properties of the square, taking into account rank and file labels
        """
        from .logic.master_logic import master_button_action

        # Delete the active frame if applicable
        if self.square:
            self.square.destroy()

        # Create the frame according to the class parameters
        self.square = Frame(self.master, bg=self.color, width=80, height=80)
        self.square.grid(row=self.rank, column=self.file)

        # The display font of the chess pieces
        self.font = Font(root=self.square, family='Times', size=50)

        # Place a button over top of the frame
        Button(self.square, bg=self.color, relief='flat', text=self.piece.label, font=self.font,
               command=lambda: master_button_action(self.container, self)).place(relheight=1, relwidth=1)
