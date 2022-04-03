# square.py by Patrick J. Donnelly
from tkinter import Frame, Button, Label
from tkinter.font import Font
key = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

# While originally intended to be a simple container for Button() objects, since Tkinter doesn't allow pixel
# modification of Button() objects, the object now houses each a frame and a button.

class Square:
    """An abstraction of a chessboard square to hold Piece() objects with TkInterface properties"""
    def __init__(self, master: Frame, container, rank: int, file: int, rank_label=False, file_label=False):
        from .logic.initialization import get_piece, get_color

        self.master = master
        self.container = container

        self.rank = rank
        self.file = file
        self.rank_label = rank_label
        self.file_label = file_label

        self.color_palate = get_color(rank, file)
        self.piece = get_piece(rank, file)
        self.font = None

        self.square = None
        self.button = None

        self.is_inverted = False

        self.set_square()

    def set_square(self):
        """
        Set the initial properties of the square, taking into account rank and file labels
        """
        # Create the frame according to the class parameters
        self.square = Frame(self.master, bg=self.get_color(), width=80, height=80)
        self.square.grid(row=self.rank, column=self.file)

        # The display font of the chess pieces
        self.font = Font(root=self.square, family='Times', size=50)

        self.set_button()

    def set_button(self):
        """
        Sets the overlay button for the square
        :return:
        """
        from .logic.master_logic import master_button_action

        self.button = Button(self.square, bg=self.get_color(), relief='flat', text=self.piece.label, font=self.font,
                             command=lambda: master_button_action(self))

        self.button.place(relheight=1, relwidth=1)

        self.set_label()

    def set_label(self):
        """
        Sets the label of the button, there is any
        """
        if self.rank_label:
            if self.container.is_flipped:
                Label(self.button, bg=self.get_color(), text=key[self.file]).place(relx=0, rely=0)
            else:
                Label(self.button, bg=self.get_color(), text=key[self.file]).place(relx=.80, rely=.70)

        if self.file_label:
            if self.container.is_flipped:
                Label(self.button, bg=self.get_color(), text=str(8 - self.rank)).place(relx=.80, rely=.70)
            else:
                Label(self.button, bg=self.get_color(), text=str(8-self.rank)).place(relx=0, rely=0)

    def update(self):
        """
        Updates the properties of a given square
        """
        from .logic.master_logic import master_button_action

        # Button automatically destroyed
        self.square.destroy()
        self.square = Frame(self.master, bg=self.get_color(), width=80, height=80)

        if self.container.is_flipped:
            # Flipping twice, once over each axis, is equivalent to a 180-degree rotation
            row = 7-self.rank
            col = 7-self.file
        else:
            row = self.rank
            col = self.file

        self.square.grid(row=row, column=col)

        # Place a button over top of the frame
        self.set_button()

    def get_color(self) -> str:
        """
        Returns the correct color for whether the square is inverted or not
        :return: A string representing the appropriate color for the square
        """
        if self.is_inverted:
            return self.color_palate[1]
        else:
            return self.color_palate[0]

    def __str__(self):
        """
        Defines the string of a square
        :return: The string representation of a given square
        """
        return str(self.piece) + key[self.file] + str(8 - self.rank)
