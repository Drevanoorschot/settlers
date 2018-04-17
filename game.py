from tkinter import Tk, Canvas

from exceptions import InvalidPlayerCountException
from model.board import Board
from model.player import Player
from view.board import draw_board
from view.color import Color


class Game:
    def __init__(self, player_count):
        if player_count not in [3, 4]:
            raise InvalidPlayerCountException()
        self.players = []
        for i in range(0, player_count):
            player = Player(i)
            self.players.append(player)
        self.board = Board()
        self.screen = Tk()

    def run(self):
        self.init()

    def init(self):
        self.screen.title("Settlers")
        board_frame = Canvas(self.screen, bg=Color.BLUE.value, width=1000, height=1000)
        board_frame.grid(row=0, column=0)
        draw_board(self.board, board_frame)
        self.screen.mainloop()
