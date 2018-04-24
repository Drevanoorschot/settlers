from tkinter import Button, Frame, PhotoImage, Label

from controller.controller import Controller
from view.board import BoardView
from view.overlay import EdgeOverlay, NodeOverlay

resource_path = "graphics/resources"
dice_path = "graphics/dice"


class GUI:
    def __init__(self, game, player):
        self.screen = game.screen
        self.dice = game.dice
        self.player = player
        self.board = game.board
        self.controller = Controller(self, game)

        self.dice_button = None
        self.end_turn_button = None

        self.grain_count = None
        self.ore_count = None
        self.brick_count = None
        self.wood_count = None
        self.wool_count = None

        self.dice_1 = None
        self.dice_2 = None
        self.board_view = BoardView(self.screen, self.board)

        self.road_overlay = EdgeOverlay(self.board, self.board_view, self.player)
        self.node_overlay = NodeOverlay(self.board, self.board_view, self.player)

        self.right_frame = Frame(self.screen)
        self.right_frame.grid(row=0, column=1)
        self.load_images()
        self.build_right_side_pane()

    def build_top_button_row(self):
        button_frame = Frame(self.right_frame)
        button_frame.grid(row=0, column=1)
        self.dice_button = Button(button_frame, command=lambda: self.dice.roll(self), text="Roll Dice")
        self.end_turn_button = Button(button_frame, command=lambda: self.controller.end_turn(), text="End Turn")
        self.dice_button.grid(row=0, column=0)
        self.end_turn_button.grid(row=0, column=1)

    def build_dice_frame(self):
        dice_frame = Frame(self.right_frame)
        dice_frame.grid(row=2, column=1)
        if self.dice.d1 is not None and self.dice.d2 is not None:
            self.dice_1 = Label(dice_frame, image=self.right_frame.dice[self.dice.d1 - 1]).grid(row=0, column=0)
            self.dice_2 = Label(dice_frame, image=self.right_frame.dice[self.dice.d2 - 1]).grid(row=0, column=1)
        else:
            Label(dice_frame, image=self.right_frame.dice[5]).grid(row=0, column=0)
            Label(dice_frame, image=self.right_frame.dice[5]).grid(row=0, column=1)
        return dice_frame

    def build_right_side_pane(self):
        self.build_top_button_row()
        self.build_resource_frame()
        self.build_dice_frame()

    def build_resource_frame(self):
        resource_frame = Frame(self.right_frame)
        resource_frame.grid(row=1, column=1)
        Label(resource_frame, image=self.right_frame.grain).grid(row=0, column=0)
        Label(resource_frame, image=self.right_frame.ore).grid(row=1, column=0)
        Label(resource_frame, image=self.right_frame.brick).grid(row=2, column=0)
        Label(resource_frame, image=self.right_frame.wood).grid(row=3, column=0)
        Label(resource_frame, image=self.right_frame.wool).grid(row=4, column=0)
        self.grain_count = Label(resource_frame, text=self.player.resources["grain"]).grid(row=0, column=1)
        self.ore_count = Label(resource_frame, text=self.player.resources["ore"]).grid(row=1, column=1)
        self.brick_count = Label(resource_frame, text=self.player.resources["brick"]).grid(row=2, column=1)
        self.wood_count = Label(resource_frame, text=self.player.resources["wood"]).grid(row=3, column=1)
        self.wool_count =Label(resource_frame, text=self.player.resources["wool"]).grid(row=4, column=1)
        return resource_frame

    def load_images(self):
        # resources
        self.right_frame.grain = PhotoImage(file="{}/grain.png".format(resource_path))
        self.right_frame.ore = PhotoImage(file="{}/ore.png".format(resource_path))
        self.right_frame.brick = PhotoImage(file="{}/brick.png".format(resource_path))
        self.right_frame.wood = PhotoImage(file="{}/wood.png".format(resource_path))
        self.right_frame.wool = PhotoImage(file="{}/wool.png".format(resource_path))

        # dice sides
        self.right_frame.dice = []
        self.right_frame.dice.append(PhotoImage(file="{}/1.png".format(dice_path)))
        self.right_frame.dice.append(PhotoImage(file="{}/2.png".format(dice_path)))
        self.right_frame.dice.append(PhotoImage(file="{}/3.png".format(dice_path)))
        self.right_frame.dice.append(PhotoImage(file="{}/4.png".format(dice_path)))
        self.right_frame.dice.append(PhotoImage(file="{}/5.png".format(dice_path)))
        self.right_frame.dice.append(PhotoImage(file="{}/6.png".format(dice_path)))
