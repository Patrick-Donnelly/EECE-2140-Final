# square.py by Patrick J. Donnelly
from tkinter import Frame, Button, Label
from tkinter.font import Font
from .logic.initialization import get_color, get_piece

# A universal key which translates file number into file letters
key = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

# While originally intended to be a simple container for Button() objects, since Tkinter doesn't allow pixel
# modification of Button() objects, the object now houses each a frame and a button.

class Square:
    """An abstraction of a chessboard square to hold Piece() objects with TkInterface properties"""
    def __init__(self, master, container, logic, rank: int, file: int, has_rank_label=False, has_file_label=False):
        """
        Creates a square object
        :param master: The Tkinter container of the square
        :param container: The superior Board() object
        :param logic: The BoardLogic() object of the superior Board()
        :param rank: The rank of the square
        :param file: The file of the Square
        :param has_rank_label: A Boolean signaling whether the square's rank should be labeled
        :param has_file_label: A Boolean signaling whether the square's file should be labeled
        """
        self.master = master
        self.container = container
        self.logic = logic

        # By convention: rank = row, file = column
        self.rank = rank
        self.file = file

        # Boolean; states whether the square should have its rank and/or file labeled
        self.has_rank_label = has_rank_label
        self.has_file_label = has_file_label

        # Initializes the square with the appropriate piece of the appropriate team via .logic.initialization functions
        self.color_palette = get_color(rank, file)
        self.piece = get_piece(rank, file)
        self.font = None

        # Placeholders for the tkinter.Frame() and tkinter.Button() objects
        self.square = None
        self.button = None

        # Controls square highlight
        self.is_highlighted = False
        self.in_check = False

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

        self.button = Button(self.square, bg=self.get_color(), activebackground=self.get_color(),
                             relief='flat', text=self.piece.label, font=self.font,
                             command=lambda: self.logic.master_button_action(self))

        self.button.place(relheight=1, relwidth=1)

        self.set_label()

    def set_label(self):
        """
        Sets the label of the button, if there is any
        """
        if self.has_rank_label:
            label = self.get_label(True)
            if self.container.is_flipped:
                label.place(relx=0, rely=0)
            else:
                label.place(relx=.80, rely=.70)

        if self.has_file_label:
            label = self.get_label(False)
            if self.container.is_flipped:
                label.place(relx=.80, rely=.70)
            else:
                label.place(relx=0, rely=0)

    def get_label(self, is_rank: bool) -> Label:
        """
        Condenses the Label() definition to a single line
        :param is_rank: A simple Boolean switch to avoid two separate functions
        :return: The desired Label() objects
        """
        txt = key[self.file] if is_rank else str(8 - self.rank)
        return Label(self.button, bg=self.get_color(), text=txt)

    def update(self):
        """
        Updates the properties of a given square
        """
        # Button automatically destroyed and redrawn; cannot ever be empty
        self.square.destroy()
        self.square = Frame(self.master, bg=self.get_color(), width=80, height=80)

        if self.container.is_flipped:
            # Flipping twice, once over each axis, is equivalent to a 180-degree rotation
            row = 7-self.rank
            col = 7-self.file
        else:
            row = self.rank
            col = self.file

        # Draws the square at the appropriate relative coordinates
        self.square.grid(row=row, column=col)

        # Place a button over top of the frame
        self.set_button()

    def get_color(self):
        """
        Returns the correct color for whether the square is inverted or not
        :return: A string representing the appropriate color for the square
        """
        if self.in_check:
            return self.color_palette[2]
        elif self.is_highlighted:
            return self.color_palette[1]
        else:
            return self.color_palette[0]

    def __str__(self):
        """
        Defines the string of a square
        :return: The string representation of a given square
        """
        return str(self.piece) + key[self.file] + str(8 - self.rank)
