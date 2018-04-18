from random import randint


class Controller:
    def __init__(self, gui, game):
        self.dice = Dice()
        self.gui = gui
        self.game = game

    def end_turn(self):
        self.gui.dice_button.config(state="normal")
        self.gui.end_turn_button.config(state="disabled")
        self.game.turns += 1


class Dice:
    d1 = None
    d2 = None

    def roll(self, gui):
        self.d1 = randint(1, 6)
        self.d2 = randint(1, 6)
        gui.dice_button.config(state="disabled")
        gui.end_turn_button.config(state="normal")
        gui.build_dice_frame()
