from random import randint
from tkinter import DISABLED


class Dice:
    d1 = None
    d2 = None

    def roll(self, gui):
        self.d1 = randint(1, 6)
        self.d2 = randint(1, 6)
        gui.build_dice_frame()
        gui.dice_button.state = DISABLED
