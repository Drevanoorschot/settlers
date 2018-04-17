from random import shuffle
from tkinter import Tk, Canvas

from exceptions import InvalidPlayerCountException
from model.board import Board
from controller.controller import Dice
from model.player import Player
from view.board import build_board
from view.color import Color
from view.view import build_gui


class Game:
    def __init__(self, player_count):
        if player_count not in [1, 3, 4]:
            raise InvalidPlayerCountException()
        self.players = []
        for i in range(0, player_count):
            player = Player(i)
            self.players.append(player)
        shuffle(self.players)
        self.board = Board()
        self.dice = Dice()
        self.screen = Tk()

    def run(self):
        self.init()

    def init(self):
        self.screen.title("Settlers")
        build_gui(self.screen, self.dice, self.players[0], self.board)
        self.screen.mainloop()
