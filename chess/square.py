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
        self.piece = get_piece(rank, file)
        self.font = None

        self.square = None

        self.set_square()

    def set_square(self):
        """
        Set the initial properties of the square, taking into account rank and file labels
        """
        from .logic.master_logic import master_button_action

        # Create the frame according to the class parameters
        self.square = Frame(self.master, bg=self.color, width=80, height=80)
        self.square.grid(row=self.rank, column=self.file)

        # The display font of the chess pieces
        self.font = Font(root=self.square, family='Times', size=50)

        # Place a button over top of the frame
        Button(self.square, bg=self.color, relief='flat', text=self.piece.label, font=self.font,
               command=lambda: master_button_action(self.container, self)).place(relheight=1, relwidth=1)

    def update_square(self):
        """
        Updates the properties of a given square
        """
        from .logic.master_logic import master_button_action

        # Button automatically destroyed
        self.square.destroy()
        self.square = Frame(self.master, bg=self.color, width=80, height=80)

        if self.container.is_flipped:
            row = 7-self.rank
            col = 7-self.file
        else:
            row = self.rank
            col = self.file

        self.square.grid(row=row, column=col)

        Button(self.square, bg=self.color, relief='flat', text=self.piece.label, font=self.font,
               command=lambda: master_button_action(self.container, self)).place(relheight=1, relwidth=1)
