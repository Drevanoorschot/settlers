from tkinter import Button, Frame, PhotoImage, Label, NW

from view.board import build_board

resource_path = "graphics/resources"
dice_path = "graphics/dice"


def build_gui(screen, dice, player, board):
    build_board(board, screen)
    right_frame = Frame(screen)
    right_frame.grid(row=0, column=1)
    load_images(right_frame)
    build_right_side_pane(right_frame, player, dice)


def build_top_button_row(frame, dice):
    button_frame = Frame(frame)
    button_frame.grid(row=0, column=1)
    dice_button = Button(button_frame, command=lambda: dice.roll(frame, build_dice_frame), text="Roll Dice")
    end_turn_button = Button(button_frame, text="End Turn")
    dice_button.grid(row=0, column=0)
    end_turn_button.grid(row=0, column=1)


def build_dice_frame(frame, dice):
    dice_frame = Frame(frame)
    dice_frame.grid(row=2, column=1)
    if dice.d1 is not None and dice.d2 is not None:
        Label(dice_frame, image=frame.dice[dice.d1 - 1]).grid(row=0, column=0)
        Label(dice_frame, image=frame.dice[dice.d2 - 1]).grid(row=0, column=1)
    else:
        Label(dice_frame, image=frame.dice[5]).grid(row=0, column=0)
        Label(dice_frame, image=frame.dice[5]).grid(row=0, column=1)


def build_right_side_pane(frame, player, dice):
    build_top_button_row(frame, dice)
    build_resource_frame(player, frame)
    build_dice_frame(frame, dice)


def build_resource_frame(player, frame):
    resource_frame = Frame(frame)
    resource_frame.grid(row=1, column=1)
    Label(resource_frame, image=frame.grain).grid(row=0, column=0)
    Label(resource_frame, image=frame.ore).grid(row=1, column=0)
    Label(resource_frame, image=frame.brick).grid(row=2, column=0)
    Label(resource_frame, image=frame.wood).grid(row=3, column=0)
    Label(resource_frame, image=frame.wool).grid(row=4, column=0)
    Label(resource_frame, text=player.resources["grain"]).grid(row=0, column=1)
    Label(resource_frame, text=player.resources["ore"]).grid(row=1, column=1)
    Label(resource_frame, text=player.resources["brick"]).grid(row=2, column=1)
    Label(resource_frame, text=player.resources["wood"]).grid(row=3, column=1)
    Label(resource_frame, text=player.resources["wool"]).grid(row=4, column=1)


def load_images(frame):
    # resources
    frame.grain = PhotoImage(file="{}/grain.png".format(resource_path))
    frame.ore = PhotoImage(file="{}/ore.png".format(resource_path))
    frame.brick = PhotoImage(file="{}/brick.png".format(resource_path))
    frame.wood = PhotoImage(file="{}/wood.png".format(resource_path))
    frame.wool = PhotoImage(file="{}/wool.png".format(resource_path))

    # dice sides
    frame.dice = []
    frame.dice.append(PhotoImage(file="{}/1.png".format(dice_path)))
    frame.dice.append(PhotoImage(file="{}/2.png".format(dice_path)))
    frame.dice.append(PhotoImage(file="{}/3.png".format(dice_path)))
    frame.dice.append(PhotoImage(file="{}/4.png".format(dice_path)))
    frame.dice.append(PhotoImage(file="{}/5.png".format(dice_path)))
    frame.dice.append(PhotoImage(file="{}/6.png".format(dice_path)))
